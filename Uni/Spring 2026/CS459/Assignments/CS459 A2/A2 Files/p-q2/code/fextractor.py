import os
import argparse
from tqdm import tqdm

    # Here you should add more features to the feature vector (features=[]) representing a cell trace

    # Function extract receives as input two sequences:
    #    times: timestamp of each cell
    #    sizes: direction of each cell (-1 / +1)

    # As of now, the only feature being used to distinguish between page loads is the total
    # amount of cells in each cell sequence and is given by len(times).

    # Should some feature be missing due to impossibility of its calculation, 
    # please replace its value with "X". It will be replaced later.

def extract(times, sizes):
    features = []

    total_cells = len(times)
    outgoing_cells = sum(1 for s in sizes if s == 1)
    trace_duration = times[-1] - times[0] if times else "X"
    direction_switches = sum(1 for a, b in zip(sizes, sizes[1:]) if a != b)
    outgoing_fraction = outgoing_cells / total_cells if total_cells else "X"
    normalized_switches = direction_switches / total_cells if total_cells else "X"

    prefix_len = 30
    prefix_sizes = sizes[:prefix_len]
    prefix_times = times[:prefix_len]

    prefix_direction_switches = sum(1 for a, b in zip(prefix_sizes, prefix_sizes[1:]) if a != b)
    prefix_duration = prefix_times[-1] - prefix_times[0] if prefix_times else "X"

    first20_sizes = sizes[:20]
    first50_sizes = sizes[:50]
    mid_sizes = sizes[30:100]
    last50_sizes = sizes[-50:] if sizes else []
    first20_outgoing_cells = sum(1 for s in first20_sizes if s == 1)
    first20_incoming_cells = sum(1 for s in first20_sizes if s == -1)
    first50_outgoing_cells = sum(1 for s in first50_sizes if s == 1)
    first50_incoming_cells = sum(1 for s in first50_sizes if s == -1)
    mid_outgoing_cells = sum(1 for s in mid_sizes if s == 1)
    mid_incoming_cells = sum(1 for s in mid_sizes if s == -1)
    last50_outgoing_cells = sum(1 for s in last50_sizes if s == 1)
    last50_incoming_cells = sum(1 for s in last50_sizes if s == -1)

    # How many cells until we see the first cell of the opposite direction?
    outgoing_before_first_incoming = "X"
    incoming_before_first_outgoing = "X"
    if sizes:
        seen_incoming = False
        count = 0
        for s in sizes:
            if s == -1:
                seen_incoming = True
                break
            count += 1
        outgoing_before_first_incoming = count if seen_incoming else "X"

        seen_outgoing = False
        count = 0
        for s in sizes:
            if s == 1:
                seen_outgoing = True
                break
            count += 1
        incoming_before_first_outgoing = count if seen_outgoing else "X"

    gaps = [t2 - t1 for t1, t2 in zip(times, times[1:])]
    mean_gap = sum(gaps) / len(gaps) if gaps else "X"
    max_gap = max(gaps) if gaps else "X"
    # Compute stddev without importing extra dependencies.
    if gaps:
        mu = mean_gap
        variance = sum((g - mu) * (g - mu) for g in gaps) / len(gaps)
        gap_std = variance ** 0.5
    else:
        gap_std = "X"

    prefix_duration_ratio = (
        prefix_duration / trace_duration
        if prefix_duration != "X" and trace_duration != "X" and trace_duration != 0
        else "X"
    )

    longest_outgoing_run = 0
    longest_incoming_run = 0
    current_outgoing_run = 0
    current_incoming_run = 0
    for s in sizes:
        if s == 1:
            current_outgoing_run += 1
            current_incoming_run = 0
        else:
            current_incoming_run += 1
            current_outgoing_run = 0
        if current_outgoing_run > longest_outgoing_run:
            longest_outgoing_run = current_outgoing_run
        if current_incoming_run > longest_incoming_run:
            longest_incoming_run = current_incoming_run

    outgoing_run_ratio = (
        longest_outgoing_run / total_cells if total_cells else "X"
    )
    incoming_run_ratio = (
        longest_incoming_run / total_cells if total_cells else "X"
    )

    # Append features
    features.append(total_cells)
    features.append(trace_duration)
    features.append(outgoing_fraction)
    features.append(normalized_switches)
    features.append(first20_outgoing_cells)
    features.append(first20_incoming_cells)
    features.append(prefix_direction_switches)
    features.append(prefix_duration)
    features.append(first50_outgoing_cells)
    features.append(first50_incoming_cells)
    features.append(mid_outgoing_cells)
    features.append(mid_incoming_cells)
    features.append(last50_outgoing_cells)
    features.append(last50_incoming_cells)
    features.append(outgoing_before_first_incoming)
    features.append(incoming_before_first_outgoing)
    features.append(mean_gap)
    features.append(max_gap)
    features.append(gap_std)
    features.append(prefix_duration_ratio)
    features.append(longest_outgoing_run)
    features.append(longest_incoming_run)
    features.append(outgoing_run_ratio)
    features.append(incoming_run_ratio)

    return features


def impute_missing(x):
        """Accepts a list of features containing 'X' in
        place of missing values. Replaces 'X' with -1.
        """
        for i in range(len(x)):
            if x[i] == 'X':
                x[i] = -1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract feature vectors')
    parser.add_argument('--traces', type=str, help='Original traces directory.',
                        required=True)
    parser.add_argument('--out', type=str, help='Output directory for features.',
                        required=True)
    args = parser.parse_args()

    if not os.path.isdir(args.out):
        os.makedirs(args.out)

    # this takes quite a while
    print("Gathering features for monitored sites...")
    for site in tqdm(range(0, 100)):
        for instance in range(0, 90):
            fname = str(site) + "-" + str(instance)
            # Set up times, sizes
            f = open(args.traces + "/" + fname, "r")
            times = []
            sizes = []
            for x in f:
                x = x.split("\t")
                times.append(float(x[0]))
                sizes.append(int(x[1]))
            f.close()
    
            # Extract features. All features are non-negative numbers or X. 
            features = extract(times, sizes)

            # Replace X by -1
            impute_missing(features)

            fout = open(args.out + "/" + fname + ".features", "w")
            for x in features[:-1]:
                fout.write(repr(x) + ",")
            fout.write(repr(features[-1]))
            fout.close()

    print("Finished gathering features for monitored sites.")
  
    f.close()
