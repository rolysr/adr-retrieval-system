from base_models.retrieval_system import RetrievalSystem
from utils.crawler import Crawler
from utils.query_expansion import query_expansion_by_synonyms
from utils.vector_feedback import classical_vector_feedback, rocchio_algorithm
import utils.metrics as metrics

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

    def query_model_name(self, query, model_name):
        """
        Receives a query and a model name and return the result of a query by 
        using a model with the specified name
        Arguments:
        query {string} -- A query string
        model_name {string} -- The name of the retrival model to be used 
        Retuns:
        query_response -- The corresponding query result
        """
        m = None
        for model in self.models:
            if model.name == model_name:
                m = model
                break
        
        if m is None:
            raise Exception('No model with the given name in the system')

        return self.query(query, m)

    def add_crawler_corpus(self, seed_url, no_of_docs):
        """
            Add <no_of_docs> files to the system corpus and model corpuses
            for getting more files
            Arguments:
            seed_url {string} -- Seed url for the crawler to work
            no_of_docs {int} -- Number of documents to add from the Crawler
        """
        crawler = Crawler(seed_url, no_of_docs)
        new_docs = crawler.get_documents()
        self.corpus.extend(new_docs)

    def get_query_expansion(self, query):
        """
            Get an expansion for a given query by generating
            words synonyms
            Arguments:
            query {string} -- query
            Results:
            query -- A new query string with added synonyms
        """
        return query_expansion_by_synonyms(query)

    def basic_feedback(self, query_vector):
        """
            Get a basic feedback for a given query
            Arguments:
            query_vector {np.array} -- a query vector
            Returns:
            new_query_vector -- A query vector that has a better chance to get better results
        """
        return classical_vector_feedback(query_vector)

    def rocchio_feedback(self, query_vector):
        """
            Get a rocchio-based feedback for a given query
            Arguments:
            query_vector {np.array} -- a query vector
            Returns:
            new_query_vector -- A query vector that has a better chance to get better results
        """
        return rocchio_algorithm(query_vector)

    def k_documents_query_model(self, query, model_name, k=20):
        """
        Receives a query and a model name and return the result of a query by 
        using a model with the specified name
        Arguments:
        query {string} -- A query string
        model_name {string} -- The name of the retrival model to be used 
        Retuns:
        query_response -- The corresponding query result
        """
        query_response = self.query_model_name(query, model_name)
        return query_response[:k] if len(query_response) >= k else query_response

    def get_metrics(self, RR, REC, REL, RRD):
        """
            Calculate metrics inside a dict()
        """

        # Get al metrics values
        precision = metrics.precision(RR, REC)
        recall = metrics.recall(RR, REL)
        f_score = metrics.f_score(RR, REL, REC, Beta=1.5)
        f1_score = metrics.f_score(RR, REL, REC)
        r_precision = metrics.r_precision(RR, REC, REL)
        novelty_ratio = metrics.novelty_ratio(RRD, RR)

        # Make response dict()
        resp = dict()
        resp['precision'] = precision
        resp['recall'] = recall
        resp['f_score'] = f_score
        resp['f1_score'] = f1_score
        resp['r_precision'] = r_precision
        resp['novelty_ratio'] = novelty_ratio

        return resp

