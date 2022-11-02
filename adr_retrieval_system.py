from base_models import RetrievalSystem

class AdrRetrievalSystem(RetrievalSystem):
    """
        A class that represents the Adr Retrieval System Core Engine
    """

    def __init__(self, corpus, models):
        """
        This constructor receives a corpus and a list of models and initilize
        the engine.
        Arguments:
        corpus {list(Document)} -- A list of all documents indexed on the corpus
        models {list(RetrievalModel)} -- A list of retrieval models
        """
        super().__init__(corpus, models)

    def query_model_name(query, model_name):
        """
        Receives a query and a model name and return the result of a query by 
        using a model with the specified name
        Arguments:
        name = 
        """