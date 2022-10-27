from utils.preprocessor import Preprocessor
from retrieval_models.vector_space_model.vector_space_model import VectorSpaceModel

if __name__ == "__main__":
    dp = Preprocessor('./dataset')
    docs = dp.generate_preprocessed_documents()
    vsm = VectorSpaceModel(docs)
    doc = vsm.parse_document(vsm.corpus[0].text)
    query = vsm.parse_query("an experimental study of a wing in a propeller")
    print(doc.document_vector, query.query_vector)
    print(vsm.sim(doc, query))