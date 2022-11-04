from base_models.retrieval_model import RetrievalModel

class RetrievalSystem:
    """
        General purpose class to represent 
        an information retrieval system engine
    """

    def __init__(self, corpus, models) -> None:
        """
            The class constructor
            Arguments:
            corpus list(document): A list of all documents from the corpus
            models list(retrieva_model): A list of retrievall models 
            that will be used by the system
        """
        # set main fields
        self.corpus = corpus
        self.models = models

    def query(self, query, model : RetrievalModel):
        """
            Receives a query string and returns a set of documents 
            that are relevant for the query and 
            Arguments:
            query {string} -- A string that represents the query
            model {retrieval_model} -- name of model to be used
            Returns:
            (list(documents), similarity) -- A list of recovered documents and
            recovery similarity
        """
        query_response = []

        # for each document calculate similarity respect to the query using the given model 
        for document in self.corpus:
            d = model.parse_document(document.text) # document
            q = model.parse_query(query) # query
            similarity = model.sim(d, q)
            query_response.append((similarity, document))
        
        query_response.sort()
        return query_response