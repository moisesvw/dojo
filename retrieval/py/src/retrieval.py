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

    def k_nearset_neighbor(self, x, docs, k=1, debug_steps=True):
        if debug_steps:
            steps = 1
        nearests = [ (q, np.inf) for q in docs[:k] ]

        for doc in docs:
            if debug_steps:
                steps += 1

            doc_distance = self.distance(x, doc)

            for i in range(k):
                if debug_steps:
                    steps += 1

                i_distance = nearests[i][1]
                if doc_distance < i_distance:
                    if debug_steps:
                        steps += 1
                    nearests.insert(i, (doc, doc_distance))
                    nearests = nearests[:k]
                    break

        print("Debugging steps", steps)
        return nearests

    def distance(self, q1, q2):
        if None in [q1, q2]:
            return np.inf

        return np.sqrt(np.sum( (q2 - q1)**2 ) )

        