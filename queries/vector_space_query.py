from collections import Counter
from queries.query import Query
import numpy as np

class VectorSpaceQuery(Query):
    """
        Class that represents a Query type for Vector Space Model
    """

    def __init__(self, query, vocab, no_of_docs, df):
        # set the query data to super class    
        super().__init__(query)

        # vectorize the input query tokens
        self.query_vector = self.gen_vector(query, vocab, no_of_docs, df) 

    def gen_vector(self, query, vocab, no_of_docs, df, a=0.5):
        """
        Create the query vector
        Arguments:
            query {string} -- query string to be parsed
            vocab {list(string)} -- all the terms in corpus
            no_of_docs {int} -- number of docs
            df -- def data structure
            a {float} -- term of soft
        Returns:
            numpy.ndarray -- vector of tokens
        """
        tokens = query.split()

        Q = np.zeros((len(vocab)))
    
        counter = Counter(tokens)
        max_freq = max([counter[token]])
        
        for token in np.unique(tokens):
            
            tf = counter[token]/max_freq
            df = df[token] if token in vocab else 0
            idf = np.log((no_of_docs+1)/(df+1))

            try:
                ind = vocab.index(token)
                Q[ind] = (a + (1-a)*tf)*idf
            except:
                pass
        return Q