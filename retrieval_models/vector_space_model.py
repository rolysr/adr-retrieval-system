from collections import Counter
from documents.vector_space_document import VectorSpaceDocument
from retrieval_models.retrieval_model import RetrievalModel
from queries.vector_space_query import VectorSpaceQuery
import numpy as np

class VectorSpaceModel(RetrievalModel):
    """
        Class that represents a vector space model
    """

    def __init__(self, corpus) -> None:
        # get the corpus data
        super().__init__(corpus)

        # calculate df
        self.df = self.get_df(corpus)

        # create vocabulary list of all unique words
        self.vocab = [term for term in self.df]

    def get_df(self, corpus):
        """
        Create a dictionary of key-value pairs where tokens 
        are keys and their occurence in the corpus the value
        Arguments:
            corpus {list(documents)} -- all documents
        Returns:
            df -- Df data structure
        """
        df = {}

        for i in range(corpus):
            tokens = corpus[i].split()
            for w in tokens:
                try:
                    # add token as key and doc number as value is chained
                    df[w].add(i)
                except:
                    # to handle when a new token is encountered
                    df[w] = {i}

        for i in df:
            # convert to number of occurences of the token from list of documents where token occurs
            df[i] = len(df[i])  

        return df

    def parse_query(self, query):
        return VectorSpaceQuery(query, self.vocab, len(self.corpus), self.df)

    def parse_document(self, document):
        return VectorSpaceDocument(document, len(self.corpus), self.df, self.vocab)

    def sim(self, document : VectorSpaceDocument, query : VectorSpaceQuery):
        cos_sim = np.dot(document, query)/(np.linalg.norm(document)*np.linalg.norm(query))
        return cos_sim

    