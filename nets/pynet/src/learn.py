import numpy as np
from .activations import Activations

class Learn(object):
    def __init__(self):
        self.activations = Activations()

    def gradient_descent(self):
        return 1

    def logistic_regression(self, x):
        nx, m = x.shape
        W = np.random.rand(m, nx)
        b = 0

        y = np.dot(W, x) + b
        return self.activations.sigmoid(y)

    def logistic_loss(self, y=0, y_hat=0.1):
        return - ( y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat) )