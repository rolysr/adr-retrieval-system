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