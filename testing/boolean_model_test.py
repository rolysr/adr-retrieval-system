from retrieval_models.boolean_model.boolean_model import *

def run_boolean_model_test():
    # Init preprocessor
    preprocessor = Preprocessor('./datasets/cranfield')

    # Get all corpus
    corpus = preprocessor.generate_preprocessed_documents()

    # Init boolean model
    bm = BooleanModel(corpus)

    # Make a query for a document
    doc = corpus[0].text
    query = "wing | proppeller"

    # Parse query and document
    d = bm.parse_document(doc)
    q = bm.parse_query(query)

    s = bm.sim(d, q)
    print(s)