from src.retrieval import Retrieval
import numpy.testing as npt
import numpy as np

class TestPyRetrieval(object):

    def test_one_nearest_neighbor(self):
        r = Retrieval()
        x = 3.0
        docs = [1.0, 2.0, 3.1, 4.0]
        assert( 3.1 == r.one_nearest_neighbor(x, docs)[0] )

    def test_k_nearest_neighbor(self):
        r = Retrieval()
        x = 9.0
        docs = np.array([5.0, 8.0, 9.2, 9.3, 9.9, 8.5, 13.0, 11.0, 8.9])
        k3_neighbors = [x for (x, _) in r.k_nearset_neighbor(x, docs, k=3) ]
        k6_neighbors = [x for (x, _) in r.k_nearset_neighbor(x, docs, k=6) ]
        assert([8.9, 9.2, 9.3] == k3_neighbors)
        assert([8.9, 9.2, 9.3, 8.5, 9.9, 8.0 ] == k6_neighbors)

    def test_distance(self):
        r = Retrieval()
        assert( r.distance(None, 3) == np.inf)
        assert( r.distance(3, None) == np.inf)
        assert( r.distance(None, None) == np.inf)

