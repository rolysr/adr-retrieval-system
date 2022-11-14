from collections import Counter
from retrieval_models.generalized_vector_space_model.generalized_vector_space_document import GeneralizedVectorSpaceDocument
from retrieval_models.generalized_vector_space_model.generalized_vector_space_query import GeneralizedVectorSpaceQuery
from base_models.retrieval_model import RetrievalModel
import numpy as np
import math

class GeneralizedVectorSpaceModel(RetrievalModel):
    """
        Class that represents a vector space model
    """

    def __init__(self, corpus) -> None:
        corpus = list(corpus[0:100]) if len(corpus) > 100 else corpus
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
        mr = list(dictionary_mr.values())
        
        for i in range(len(self.vocab)):
            #sprint("i={}".format(i))
            numerator = np.zeros(len(self.vocab))
            denominator = 0
            for j in range(len(mr)):
                if mr[j][i] == 1:
                    cir = self.calculate_cir(dictionary_mr,mr[j],i)
                    numerator = numerator + cir*mr[j]
                    denominator = denominator + cir**2
            numerator = numerator/math.sqrt(denominator) if denominator > 0 else np.zeros(len(self.vocab))
            ki[self.vocab[i]] = numerator

        return ki


    def calculate_cir(self,dictionary_mr,mr,index):
        """
        Calculate Ci,r if gl(dj)==gl(Mr) for all l
        """
        cir = 0
        for i in range(len(self.corpus)):

            if np.array_equal(dictionary_mr[i],mr):
                #print("Entre aqui ",dictionary_mr[i])
                cir = cir + self.wij[i][index]
        #if cir==0:
         #   print(mr,index)
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
            mr[i] = aux

        return mr 

    def get_wij(self,corpus):
        """
        Obtain the documents matrix weith 
        """
        
        wij={}
        
        for i in range(len(corpus)):
            wij[i] = self.parse_document(corpus[i].text).document_vector
        
        return wij

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
        return GeneralizedVectorSpaceQuery(query, self.vocab, len(self.corpus), self.df)

    def parse_document(self, document):
        return GeneralizedVectorSpaceDocument(document, len(self.corpus), self.df, self.vocab)

    def sim(self, document : GeneralizedVectorSpaceDocument, query : GeneralizedVectorSpaceQuery):
        q = query.query_vector
        weight = np.zeros(len(self.vocab))
        q_weight= np.zeros(len(self.vocab))
        for i in range(len(self.corpus)):
            if self.corpus[i].text == document.text:
                for j in range(len(self.vocab)):
                    weight = weight + self.wij[i][j]*self.ki[self.vocab[j]]
                    q_weight = q_weight + q[j]*self.ki[self.vocab[j]]
                break
        cos_sim = np.dot(weight, q_weight)/(np.linalg.norm(weight)*np.linalg.norm(q_weight))
        return cos_sim

    