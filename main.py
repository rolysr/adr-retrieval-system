from retrieval_models.boolean_model.boolean_model import BooleanModel
from utils.preprocessor import Preprocessor
from retrieval_models.vector_space_model.vector_space_model import VectorSpaceModel

if __name__ == "__main__":
    dp = Preprocessor('./dataset')
    docs = dp.generate_preprocessed_documents()
    bm = BooleanModel(docs)
    query = bm.parse_query("wing | study")
    doc = bm.parse_document(bm.corpus[0].text)
    print(doc.bit_vector, query.postfix_query)
    print(bm.sim(doc, query))