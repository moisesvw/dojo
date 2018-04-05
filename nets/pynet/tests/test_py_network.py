from src.activations import Activations
import numpy.testing as npt
from src.learn import Learn 
import numpy as np

class TestPyNetwork(object):

    def test_sigmoid(self):
        a = Activations()
        assert(0.6224593312018546 == a.sigmoid(0.5))

    def test_logistic(self):
        l = Learn()
        x = np.array([[0.3, 0,3]])
        print(x.shape)
        print(l.logistic_regression(x) )

    def test_logistic_loss(self):
        l = Learn()
        y = np.array([1, 1, 0, 1, 0]).T
        y_hat = np.array([0.95, 0.87, 0.2, 0.7, 0.5]).T
        
        loss_1 = l.logistic_loss(y=y[0], y_hat=y_hat[0])
        npt.assert_almost_equal(loss_1, 0.05129, decimal=5)
        losses = l.logistic_loss(y=y, y_hat=y_hat)
        expected = np.array([0.05129, 0.13926, 0.22314, 0.35667, 0.69315]).T
        npt.assert_almost_equal(losses, expected, decimal=5)