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
    # Global traffic size and directionality.
    total_cells = len(times)
    outgoing_cells = sum(1 for s in sizes if s == 1)
    incoming_cells = sum(1 for s in sizes if s == -1)
    trace_duration = times[-1] - times[0] if times else "X"
    direction_switches = sum(1 for a, b in zip(sizes, sizes[1:]) if a != b)
    # Fraction of cells that are outgoing: interaction-heavy vs content-heavy.
    # Kept as a bounded (0..1) value, which behaves better than a raw ratio
    # in the distance-based k-NN classifier.
    outgoing_fraction = outgoing_cells / total_cells if total_cells else "X"
    normalized_switches = direction_switches / total_cells if total_cells else "X"

    # Early / mid / late window features (traffic in different load phases).
    first20_sizes = sizes[:20]
    first50_sizes = sizes[:50]
    mid_sizes = sizes[30:100]
    last50_sizes = sizes[-50:] if sizes else []

    first20_outgoing_cells = sum(1 for s in first20_sizes if s == 1)
    first50_incoming_cells = sum(1 for s in first50_sizes if s == -1)
    mid_incoming_cells = sum(1 for s in mid_sizes if s == -1)
    last50_outgoing_cells = sum(1 for s in last50_sizes if s == 1)

    # Direction-order feature: how many outgoing (request) cells are sent
    # before the first incoming (response) cell arrives.
    outgoing_before_first_incoming = "X"
    if sizes:
        seen_incoming = False
        count = 0
        for s in sizes:
            if s == -1:
                seen_incoming = True
                break
            count += 1
        outgoing_before_first_incoming = count if seen_incoming else "X"

    # Inter-arrival timing features.
    gaps = [t2 - t1 for t1, t2 in zip(times, times[1:])]
    if gaps:
        mean_gap = sum(gaps) / len(gaps)
        variance = sum((g - mean_gap) * (g - mean_gap) for g in gaps) / len(gaps)
        gap_std = variance ** 0.5
    else:
        mean_gap = "X"
        gap_std = "X"

    # Burst and run-length features.
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

    features = [
        # Global traffic size and directionality.
        total_cells,
        trace_duration,
        outgoing_fraction,
        normalized_switches,
        # Window-based traffic summaries (early / mid / late load phases).
        first20_outgoing_cells,
        first50_incoming_cells,
        mid_incoming_cells,
        last50_outgoing_cells,
        # Direction-order feature.
        outgoing_before_first_incoming,
        # Timing features.
        mean_gap,
        gap_std,
        # Burst / run-length features.
        longest_outgoing_run,
        longest_incoming_run,
    ]

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
