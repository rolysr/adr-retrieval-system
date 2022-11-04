from utils.vector_feedback import *
from retrieval_models.vector_space_model.vector_space_model import VectorSpaceModel
from utils.preprocessor import Preprocessor

def run_vector_feedback_test():
    corpus = Preprocessor('./datasets').generate_preprocessed_documents()
    vsm = VectorSpaceModel(corpus)

    doc = corpus[0].text
    qry = "wing is beatiful"

    doc = vsm.parse_document(doc)
    qry = vsm.parse_query(qry)

    sim1 = vsm.sim(doc, qry)
    print('Sim1 is ', sim1)

    qry1 = classical_vector_feedback([(doc.document_vector, True)], 1)

    print(qry1)
    qry.query_vector = qry1
    sim2 = vsm.sim(doc, qry)
    print('Sim2 is ', sim2)

    qry2 = rocchio_algorithm([(doc.document_vector, True)], qry, 1)

    print(qry2)
    qry.query_vector = qry2
    sim3 = vsm.sim(doc, qry)
    print('Sim3 is ', sim3)  