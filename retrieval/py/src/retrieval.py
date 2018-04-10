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

    def k_nearest_neighbor(self, x, docs, k=1, debug_steps=False):
        if debug_steps:
            steps = 1

        k_neighbors = docs[:k]
        k_distances = np.array([self.distance(x, d) for d in k_neighbors])
        idx = np.argsort(k_distances)
        k_neighbors = k_neighbors[idx] 
        k_distances = k_distances[idx]

        for i in range(k, docs.shape[0]):
            if debug_steps:
                steps += 1

            distance = self.distance(x, docs[i])

            if distance < k_distances[-1]:
                find_j = False
                for j in reversed(range(1, k)):
                    if distance > k_distances[j-1] and distance < k_distances[j]:
                        find_j = True
                        k_neighbors[j+1:k] = k_neighbors[j:k-1]
                        k_distances[j+1:k] = k_distances[j:k-1]
                        k_neighbors[j] = docs[i]
                        k_distances[j] = distance
                        break

                if not find_j:
                    if debug_steps:
                        steps += 1
                    j = 0
                    k_neighbors[j+1:k] = k_neighbors[j:k-1]
                    k_distances[j+1:k] = k_distances[j:k-1]
                    k_neighbors[j] = docs[i]
                    k_distances[j] = distance


        if debug_steps:
            print("Debugging steps", steps)
        return zip(k_neighbors, k_distances)

    def distance(self, q1, q2):
        if None in [q1, q2]:
            return np.inf

        return np.sqrt(np.sum( (q2 - q1)**2 ) )

        