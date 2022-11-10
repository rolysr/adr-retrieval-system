from collections import Counter
from retrieval_models.vector_space_model.vector_space_document import VectorSpaceDocument
from base_models.retrieval_model import RetrievalModel
from retrieval_models.vector_space_model.vector_space_query import VectorSpaceQuery
import numpy as np
import math

class GeneralizedVectorSpaceModel(RetrievalModel):
    """
        Class that represents a vector space model
    """

    def __init__(self, corpus) -> None:
        # get the corpus data
        super().__init__(corpus, name='GeneralizedVectorSpaceModel')

        # calculate df
        self.df = self.get_df(corpus)

        # create vocabulary list of all unique words
        self.vocab = [term for term in self.df]

        self.wij = self.get_wij(corpus)

        self.ki = self.get_ki(corpus)
 
    def get_ki(self,corpus):
        """
        Create a dictionary of key-value pairs where tokens 
        are keys and Ki are the value
        Arguments:
            corpus {list(documents)} -- all documents
        Returns:
            ki -- Ki data structure
        """
        ki = {}

        dictionary_mr = self.get_mr(corpus)
        mr = dictionary_mr.values()
        
        for i in range(len(self.vocab)):
            numerator = np.zeros(len(self.vocab))
            denominator = 0
            for j in range(len(mr)):
                if mr[j][i] == 1:
                    cir = self.calculate_cir(dictionary_mr,mr[j],i)
                    numerator = numerator + cir*mr[j]
                    denominator = denominator + cir**2
            for i in range(len(numerator)):
                numerator[i] = numerator[i]/math.sqrt(denominator)
            ki[self.vocab[i]].add(numerator)

        return ki


    def calculate_cir(self,dictionary_mr,mr,index):
        """
        Calculate Ci,r if gl(dj)==gl(Mr) for all l
        """
        for i in range(len(self.corpus)):
            cir = 0
            if dictionary_mr[i] == mr:
                cir = cir + self.wij[i][index]
        return cir

    def get_mr(self, corpus):
        """
        Create a dictionary of key-value pairs where index-documents 
        are keys and Mr are the value
        Arguments:
            corpus {list(documents)} -- all documents
        Returns:
            mr -- Mr data structure
        """
        mr = {}


        for i in range(len(corpus)):
            aux = np.zeros(len(self.vocab))
            for j in range(len(self.vocab)):
                if self.vocab[j] in corpus[i].text.split():
                    aux[j] = 1
            mr[i].add(aux)
        
        return mr 

    def get_wij(self,corpus):
        """
        Obtain the documents matrix weith 
        """
        
        wij={}
        
        for i in range(len(corpus)):
            wij[i] = self.parse_document(corpus[i].text).document_vector

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

        for i in range(len(corpus)):
            tokens = corpus[i].text.split()
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
        q = query.query_vector
        weight = np.zeros(len(self.corpus))
        for i in range(len(self.corpus)):
            if self.corpus[i].text == document.text:
                for j in self.vocab:
                    weight = weight + self.wij[i][j]*self.ki[j]
                break
        cos_sim = np.dot(weight, q)/(np.linalg.norm(weight)*np.linalg.norm(q))
        return cos_sim

    