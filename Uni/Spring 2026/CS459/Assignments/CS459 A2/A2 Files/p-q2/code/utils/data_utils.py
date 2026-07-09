import os
import csv
import json
import numpy as np
from .experiment_utils import log

def load_packet_sequence(fname):
    """Loads a packet sequence from a file.

    The file should contain, one per line, the time and size
    of each packet separated by '\t'.
    Negative sizes indicate incoming packets, positive indicate
    outgoing packets.

    A packet sequence is a list in the form:
        [[t1, s1], [t2, s2], ...],
    where ti and si are respectively the time and size of the
    i-th packet in the sequence.
    """
    ps = []
    with open(fname, 'rb') as f:
        rows = csv.reader(f, delimiter='\t')
        for time, size in rows:
            ps.append((float(time), int(size)))

    return ps


def load_features(folder):
    log('Loading features from {}'.format(folder))
    feature_vecs = []           # List of feature vectors.
    labels = []                 # List of labels (webpage ids).
    wid = []                    # List of webpage-load ids.

    files = [os.path.join(folder, x) for x in os.listdir(folder)]
    files = [x for x in files if x.endswith('.features')]

    #Hack to remove non-monitored pages
    files = [x for x in files if os.path.basename(x).find('-') != -1]

    for f in files:
        f_base = os.path.basename(f).replace('.features', '')
        # A file is considered only if its name is in the format
        # "page_id-load_id".
        page_id, load_id = f_base.split('-')
        f = np.genfromtxt(f, delimiter=',').reshape(1,-1)
        feature_vecs.append(f)
        labels.append(int(page_id))
        wid.append(f_base)

    X = np.vstack(feature_vecs)

    labels = np.array(labels)
    n_pages = len(set(labels))
    n_loads = -1

    log('Loaded {} monitored pages'.format(n_pages))
    log('Total number of samples: {}'.format(len(X)))

    return X, labels, wid, n_pages, n_loads, len(X[0])

def store_results(fname, results):
    """Stores a dictionary of results into a json file.
    """
    with open(fname, 'w') as f:
        json.dump(results, f, sort_keys=True, indent=4, separators=(',', ': '))
