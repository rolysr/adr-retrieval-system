from utils.documents_preprocessor import DocumentsPreprocessor
from retrieval_models.retrieval_model import RetrievalModel

if __name__ == "__main__":
    dp = DocumentsPreprocessor('./dataset')
    docs = dp.generate_preprocessed_documents()
    print(docs)