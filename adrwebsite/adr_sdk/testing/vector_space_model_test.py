from retrieval_models.vector_space_model.vector_space_model import *
from utils.preprocessor import *

def run_vector_space_model_test():
    # Init preprocessor
    preprocessor = Preprocessor('./datasets')

    # Get all corpus
    corpus = preprocessor.generate_preprocessed_documents()

    # Init boolean model
    vsm = VectorSpaceModel(corpus)

    # Make a query for a document
    doc = corpus[0].text
    query = "An experimental study of a wing in a propeller slipstream"

    # Parse query and document
    d = vsm.parse_document(doc)
    q = vsm.parse_query(query)

    s = vsm.sim(d, q)
    print(s)