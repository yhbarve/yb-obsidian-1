import torch
import torch.nn.functional as F
import pandas as pd
import numpy as np
import os

# ================================================
# Membership Inference Assignment
# ================================================
# Introduction:
# Membership inference attacks (MIAs) attempt to determine whether a given sample
# was part of a model's training set ("member") or not ("non-member").

# You have been provided:
#  - trained_model.pth (** 99.10% accuracy on training set **) -> trained as a multi-class classifier
#  - dataset.csv containing:
#      - 'index': original index
#      - 'pixels': space-separated 0–255 pixel values
#      - 'label': true class label (0–9)
#
# Using your WATiam ID, generate your personalized dataset and predict membership.
# ** Do NOT alter the DataFrame index—they will be used for grading. **

class SimpleCNN(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 16, 3)
        self.conv2 = torch.nn.Conv2d(16, 32, 3)
        self.fc1   = torch.nn.Linear(32 * 5 * 5, 128)
        self.fc2   = torch.nn.Linear(128, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(x, 2)
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, 2)
        x = x.view(-1, 32 * 5 * 5)
        x = F.relu(self.fc1(x))
        return self.fc2(x)

def load_full_dataset(csv_path="final_dataset_membership.csv"):
    """
    Load the full dataset CSV.
    Returns a pandas DataFrame.
    """
    
    return pd.read_csv(csv_path)


def parse_images(df):
    """
    Convert df['pixels'] into a torch.Tensor of shape (N,1,28,28), normalized to [0,1]. 
    ** Do not change this function **.
    """
    pixels = np.stack(df["pixels"].apply(lambda x: np.fromstring(x, sep=' ')).values)
    images = torch.tensor(pixels, dtype=torch.float32).view(-1, 1, 28, 28) / 255.0
    return images


def sample_dataset(df, watiam_id, sample_size=500):
    """
    Sample `sample_size` rows using your watiam_id as seed (sum of character codes). 
    ** Do not change this function **.
    """
    seed = sum(ord(c) for c in watiam_id)
    np.random.seed(seed)
    indices = np.random.choice(df.index.values, size=sample_size, replace=False)
    return df.loc[indices]


def predict_membership(model, images):
    """
    Given a model and images tensor of shape (N,1,28,28),
    run the model and infer membership (1) vs non-membership (0).
    Returns a list or numpy array of predicted membership flags(0 or 1).

    ** Hint: You can use the model's output probabilities to determine membership. **

    """

    # inference only
    with torch.no_grad():
        # Forward pass
        logits = model(images)
        # Convert logits to probabilities
        probs = F.softmax(logits, dim=1)
        # Get the maximum probability for each sample
        confidences = probs.max(dim=1).values
    # Print the confidence statistics
    print("Confidence Statistics:")
    print("Min:", confidences.min())
    print("Median:", np.median(confidences))
    print("Mean:", confidences.mean())
    print("Max:", confidences.max())
    print("--------------------------------")
    print("Confidence Threshold Statistics:")
    for t in [0.9, 0.95, 0.99]:
        print(t, (confidences >= t).sum())
    print("--------------------------------")

    # Threshold for membership inference
    threshold = 0.95
    # Create the membership labels based on the confidence scores
    predicted_labels = (confidences > threshold).int().tolist()

    return predicted_labels, confidences.tolist()


def save_outputs(df_sampled, predicted_labels, watiam_id):
    """
    Create a new DataFrame with just the index and 'is_member' predicted labels,
    then save that CSV and a text report.
    """
    # New DataFrame with index and predicted membership flag
    out_df = pd.DataFrame({'is_member': predicted_labels}, index=df_sampled.index)

    csv_name = f"{watiam_id}_predictions.csv"
    txt_name = f"{watiam_id}_approach.md"

    # Save CSV (retain original index)
    out_df.to_csv(csv_name, index=True)
    print(f"Saved predictions to {csv_name}")
    
    if (os.path.exists(txt_name)):
        print(f"Report file {txt_name} already exists, will not overwrite.")
        return

    # Write report
    with open(txt_name, 'w') as f:
        f.write("Membership Inference Report\n")
        f.write(f"WATiam ID: {watiam_id}\n")
        f.write("\nApproach:\n")
        f.write("Write your approach here\n")
    print(f"Saved report to {txt_name}")


if __name__ == "__main__":
    watiam_id = "yhbarve"  # <-- replace with your own ID, do not use capitals

    # 2. Load model
    model = SimpleCNN()
    model.load_state_dict(torch.load("trained_model.pth", map_location="cpu"))

    # 3. Load and parse full dataset
    df_full = load_full_dataset()
    images_full = parse_images(df_full)

    # 4. Sample your personalized subset
    df_sampled = sample_dataset(df_full, watiam_id, sample_size=500)
    # Use the same images array to index into tensor
    images_sampled = images_full[df_sampled.index]

    # 5. Predict membership
    predicted_labels, confidences = predict_membership(model, images_sampled)

    # 6. Save outputs
    save_outputs(df_sampled, predicted_labels, watiam_id)