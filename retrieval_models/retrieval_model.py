class RetrievalModel:
    """
        Class that represents an abstract model to define 
        new information retrieval systems models
    """

    def __init__(self, corpus):
        """
        Gets an instance of the corpus 
        Arguments:
            corpus {list(Document)} -- A corpus instance
        """     
        self.corpus = corpus 

    def parse_query(self, query):
        """
        Parse query function to convert a given query as a normal text and 
        return an instance of the query type corresponding to this Model 
        Arguments:
            query {string} -- query string to be parsed
        Returns:
            Query -- An instance of a Query corresponding to this models' format
        """
        pass

    def parse_document(self, document):
        """
        Parse document function to convert a given document and 
        return an instance of the document type corresponding to this Model 
        Arguments:
            document {string} -- document string to be parsed
        Returns:
            Document -- An instance of a Document corresponding to this models' format
        """
        pass

    def sim(self, document, query):
        """
        Similarity function of the model 
        Arguments:
            document {Document} -- Document parameter
            query {Query} -- Document parameter
        Returns:
            SimReturn -- An instance of a SimReturn corresponding to this models' format
        """
        pass