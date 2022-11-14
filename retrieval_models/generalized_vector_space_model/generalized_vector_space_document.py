from collections import Counter
from base_models.document import Document
import numpy as np

class GeneralizedVectorSpaceDocument(Document):
    """
        Class that represents a vector space document
    """

    def __init__(self, document, corpus_len, df, vocab):
        """Receives a document as necessary data for a document.
        Arguments:
            document {string} -- document main content
            tf_idf {tf_idf} -- tf_idf data structure
            vocab  -- vocab data structure
        """
        super().__init__(document)
        
        # vectorize the input document
        self.document_vector = self.gen_vector(document, corpus_len, df, vocab) 

    def gen_vector(self, document, corpus_len, df, vocab):
        """
        Create the document vector
        Arguments:
            document {string} -- document string to be parsed
            corpus_len -- tf_idf data structure
            vocab_len {len} -- vocab len
        Returns:
            numpy.ndarray -- vector of tokens
        """
        # initializing empty vector of vocabulary size
        D = np.zeros(len(vocab))

        # creating vector of tf-idf values
        tokens = document.split()

        # counter object to efficiently count number of occurence of a term in a particular document
        counter = Counter(tokens)
        max_freq = max([counter[token] for token in tokens])
        token_index = 0

        for token in np.unique(tokens):
            # counting occurence of term in object using counter object
            tf = counter[token]/max_freq
            # retrieving df values from DF dictionary
            df_value = df[token] if token in vocab else 0
            
            idf = np.log((corpus_len+1)/(df_value+1))
            D[token_index] = tf*idf
            token_index += 1
        
        return D