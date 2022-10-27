from retrieval_models.boolean_model.boolean_model import BooleanModel
from utils.preprocessor import Preprocessor
from retrieval_models.vector_space_model.vector_space_model import VectorSpaceModel

if __name__ == "__main__":
    dp = Preprocessor('./datasets')
    docs = dp.generate_preprocessed_documents()
    print(len(docs))