import argparse
import time
import sys
from attacks.attacks import KNNAttack
from utils.experiment_utils import log
from utils.data_utils import load_features
from utils.data_utils import store_results
from sklearn.model_selection import train_test_split
from utils.experiment_utils import train_test_closed_world
import numpy as np

np.set_printoptions(threshold=np.inf, linewidth=np.nan)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run an attack')
    parser.add_argument('--features', type=str, help='Features directory.',
                        required=True)
    parser.add_argument('--k', type=int,
                        help='Number of neighbours used in k-NN.',
                        required=True)
    parser.add_argument('--seed', type=int, help='PRNG seed (default: 0).',
                        required=False, default=0)
    parser.add_argument('--out', type=str, help='Output file (.json).',
                        required=True)
    args = parser.parse_args()

    X, Y, wid, Npages, Nloads, NFeatures = load_features(args.features)

    log('Number of features: {}'.format(NFeatures))
    log('Seed is {}'.format(args.seed))

    n = len(X)
    # Get training/test set size
    
    #Fixed proportion of monitored pages
    train_size = int(0.8*n)
    test_size = int(0.2*n)

    log('Adding {} monitored traces to training set'.format(train_size))
    log('Adding {} monitored traces to testing set'.format(test_size))
    if train_size + test_size != n:
        log('Note: {} instances will be excluded'.format(n - train_size - test_size))

    #log('Splitting into training/test set keeping uniform labels')
    # First get the test set
    I = range(n)                        # Indexes
    Iother, Itest = train_test_split(I, test_size=test_size, stratify=Y, random_state = args.seed)
    Xtest = X[Itest,:]
    Ytest = Y[Itest]

    # Now the training set
    # If train_size + test_size < n, sample from the remaining
    # n - test_size instances the training set
    if train_size < len(Iother):
        log('Reduced training set')
        # Strain_size instances from Iother to create the training set
        Itrain, _ = train_test_split(Iother, train_size=train_size, stratify=Y[Iother], random_state=args.seed)
    else:
        Itrain = Iother
    # Training set
    Xtrain = X[Itrain,:]
    Ytrain = Y[Itrain]

    log('Launching k-NN attack')
    attack = KNNAttack(NFeatures, args.k, "closed")

    res = attack.evaluate_attack(Xtrain, Ytrain, Xtest, Ytest)

    log('Storing results into {}'.format(args.out))
    store_results(args.out, res)

    #Allow for C external libs to be collected
    time.sleep(2)

