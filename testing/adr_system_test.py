from adr_retrieval_system import AdrRetrievalSystem
from utils.preprocessor import Preprocessor
from retrieval_models.boolean_model.boolean_model import BooleanModel
from retrieval_models.vector_space_model.vector_space_model import VectorSpaceModel

def run_adr_system_test():
    # Generate corpus
    corpus = Preprocessor('./datasets').generate_preprocessed_documents()

    # Create instances of vector space model and boolean model
    bm = BooleanModel(corpus)
    vsm = VectorSpaceModel(corpus)

    # Create an instance of ADR Retrieval System
    adr = AdrRetrievalSystem(corpus, [bm, vsm])

    # Test basic query using vsm
    query = "A wing is good"
    query_response = adr.query(query, adr.models[1])

    print(len(query_response))
    print(query_response[0])

    # Test basic query using bm
    query = "wing | house | ( ~dog & wings )"
    query_response = adr.query(query, adr.models[0])

    print(len(query_response))
    print(query_response[0:20])

    # Test query by model name
    query = "A wing is good"
    query_response = adr.query_model_name(query, "VectorSpaceModel")

    print(len(query_response))
    print(query_response[0])

    # Test query k items on the response
    query = "A wing is good"
    query_response = adr.k_documents_query_model(query, "VectorSpaceModel")

    print(query_response)