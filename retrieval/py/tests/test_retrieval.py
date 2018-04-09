from src.retrieval import Retrieval
import numpy.testing as npt
import numpy as np

class TestPyRetrieval(object):

    def test_one_nearest_neighbor(self):
        r = Retrieval()
        x = 3.0
        docs = [1.0, 2.0, 3.1, 4.0]
        assert( 3.1 == r.one_nearest_neighbor(x, docs)[0] )

    def test_distance(self):
        r = Retrieval()
        assert( r.distance(None, 3) == np.inf)
        assert( r.distance(3, None) == np.inf)
        assert( r.distance(None, None) == np.inf)

