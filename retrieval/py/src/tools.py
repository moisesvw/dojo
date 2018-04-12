import numpy as np

class Tools(object):
    def idf(self, docs, vocab):
        """
        inverse document frequency
        """
        idf = np.zeros_like(vocab, dtype=np.float32)
        num_docs = len(docs)
        for index, word in enumerate(vocab):
            n_doc_using_word = 0
            for doc in docs:
                if word in doc:
                   n_doc_using_word += 1
            idf[index] = np.log(num_docs/(1.0 + n_doc_using_word))

        return idf

    def tf(self, docs, vocab):
        """
        term frequency
        """
        tf = np.zeros_like(vocab, dtype=np.float32)

        for doc in docs:
            for w in doc.split(" "):
                idx = vocab.index(w)
                tf[idx] += 1.

        return tf