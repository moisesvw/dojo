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
        """
        The loss function for binary classification
        When expected class is 1
            log(y_hat)
        when expected clss is 0
            log(1 - y_hat)
        when predicted y_hat is far from expected
        the error will be bigger, otherwise will be smaller near 0.0
        """
        return - ( y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat) )