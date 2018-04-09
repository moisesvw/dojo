import numpy as np

class Retrieval(object):
    def one_nearest_neighbor(self, x, docs):
        nearest = None
        nearest_distance = np.inf
        for doc in docs:
            doc_distance = self.distance(x, doc)
            if doc_distance < nearest_distance:
                nearest = doc
                nearest_distance = doc_distance

        return (nearest, nearest_distance)

    def distance(self, q1, q2):
        if None in [q1, q2]:
            return np.inf

        return np.sqrt(np.sum( (q2 - q1)**2 ) )

        