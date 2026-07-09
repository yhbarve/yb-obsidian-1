from .ctypes_utils import *
from ctypes import *
import numpy as np
from ctypes import cdll
from sklearn.metrics import confusion_matrix

WANG_LIB = 'attacks/wang/flearner.so'
NAN = np.nan
ISNAN = np.isnan


class KNNAttack():
    feat_number = 0
    k_neighbours = 0
    mode = "none"

    def __init__(self, feat_number, k_neighbours, mode):
        self.libknn = cdll.LoadLibrary(WANG_LIB)
        self.feat_number = feat_number
        self.k_neighbours = k_neighbours
        self.mode = mode

    def evaluate_attack(self, train_fv, train_labels, test_fv, test_labels):

        res = {}
        pred = self.classify(train_fv, train_labels, test_fv, test_labels)
        

        FP = 0
        for i in range(0, len(test_labels)):
            if(test_labels[i] != pred[i] and pred[i] != -1):
                FP+=1
        

        FN = 0
        for i in range(0, len(test_labels)):
            if(test_labels[i] != pred[i] and pred[i] == -1):
                FN+=1

        TP = 0
        for i in range(0, len(test_labels)):
            if(test_labels[i] == pred[i] and pred[i] != -1):
                TP+=1

        TN = 0
        for i in range(0, len(test_labels)):
            if(test_labels[i] == pred[i] and pred[i] == -1):
                TN+=1
        
        #TPR: Monitored site is classified as the correct monitored
        TPR = 1. * TP / (TP + FN)

        #FPR: Non-monitored site is classified as any monitored site
        FPR = 1. * FP / (FP + TN)
        

        ACC = (TP + TN) / float(len(test_labels))
        
        print("-----------------------------------")
        print("Closed-World Analysis Metrics")
        print("-----------------------------------")
        print("Accuracy: " + str(ACC)) 

        res['tp'] = TP
        res['tn'] = TN
        res['fp'] = FP
        res['fn'] = FN
        res['tpr'] = TPR
        res['fpr'] = FPR
        res['acc'] = ACC
        res['true_labels'] = [int(x) for x in test_labels]
        res['predicted_labels'] = [int(x) for x in pred]
        return res
        

    def classify(self, train_fv, train_labels, test_fv, test_labels):
        """Returns the accuracy of the attack trained on training
        feature vectors train_fv, and performed on test_fv.
        """
        n_train = len(train_fv)
        n_test = len(test_fv)
        n_labels = len(set(test_labels))

        self.libknn.set_feature_number(c_int(self.feat_number))
        
        weights = self._recommend_weights(train_fv, train_labels)
        
        # Prepare return array.
        predictions = [-1]*n_test

        # Convert to ctypes.
        train_fv_c = list_list_to_c_float_list_list(train_fv)
        test_fv_c = list_list_to_c_float_list_list(test_fv)
        train_labels_c = list_to_c_int_list(train_labels)
        predictions_c = list_to_c_int_list(predictions)
        weights_c = list_to_c_float_list(weights)

        self.libknn.knn_predict(train_fv_c, train_labels_c, test_fv_c,
                                c_int(n_train),
                                c_int(n_test),
                                c_int(n_labels),
                                c_int(self.k_neighbours),
                                weights_c, predictions_c)

        # Get back results.
        predictions = c_list_to_list(predictions_c)

        return predictions

    def _init_weights(self, d):
        """Returns a list of initialised weights.
        Weights are initialised randomly using numpy library.
        You can set the general seed of the library if you
        want reproducible results.

        Params
        d : int
            Length of the vector of weights.
        """
        return [np.random.rand() + 0.5 for x in range(d)]


    def _recommend_weights(self, feature_vecs, labels, n_rounds=5):
        """Recommends weights for the features.
        """
        n = len(feature_vecs)
        d = len(feature_vecs[0])

        # Initialise weights.
        weights = self._init_weights(d)

        # Convert to ctypes.
        n_c = c_int(n)
        feature_vecs_c = list_list_to_c_float_list_list(feature_vecs)
        labels_c = list_to_c_int_list(labels)
        weights_c = list_to_c_float_list(weights)

        print('Learning weights for {} total rounds'.format(n_rounds))

        for r in range(n_rounds):
            print('Round {}'.format(r))
            start = n/n_rounds * r
            end = n/n_rounds * (r+1)
            # The result is put into weights_c.
            self.libknn.recommend_weight(feature_vecs_c, labels_c, n_c,
                                         weights_c,
                                         int(start),
                                         int(end))
        # Convert from ctypes.
        weights = c_list_to_list(weights_c)

        return weights
