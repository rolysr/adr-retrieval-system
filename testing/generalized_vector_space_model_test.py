from retrieval_models.generalized_vector_space_model.generalized_vector_space_model import *
from utils.preprocessor import *

def run_generalized_vector_space_model_test():
    # Init preprocessor
    preprocessor = Preprocessor('./datasets/cranfield')

    # Get all corpus
    corpus = preprocessor.generate_preprocessed_documents()

    # Init boolean model
    vsm = GeneralizedVectorSpaceModel(corpus)
    query_response = []
    query = "what similarity laws must be obeyed when constructing aeroelastic models of heated high speed aircraft"
    count =0

    for document in corpus:
        d = vsm.parse_document(document.text) # document
        q = vsm.parse_query(query) # query
        similarity = vsm.sim(d, q)
        query_response.append((similarity, document))
        
    query_response.sort()
    query_response.reverse()

    for i in query_response:
        count+=1
        print(i)
        if count==110:
            break