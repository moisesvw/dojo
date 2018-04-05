import numpy as np

class Activations(object):
    def sigmoid(self, x):
        return 1/(1 + np.exp(-x))