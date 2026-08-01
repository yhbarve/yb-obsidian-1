Membership Inference Report
WATiam ID: yhbarve

Approach:

First, I passed every sampled image through the trained CNN model. Then I converted the logits outputted by the model to class probabilities with softmax. For each image, I picked the maximum probability as a confidence score.

My approach relies on the assumption that the model performs with very high accuracy on its training data. After analyzing the confidence scores, the correct threshold to detect images from the training set is 95%. Any image with a confidence score greater than 95% has a high likelihood of belonging in the training set.

**The median confidence was 78.98%. 31 sample images exceeded the 95% confidence threshold, and 28 sample images exceeded the 99% confidence threshold.**
