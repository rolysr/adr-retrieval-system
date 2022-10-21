from documents_preprocessor import DocumentsPrepocessor

if __name__ == "__main__":
    dp = DocumentsPrepocessor('./datasets', './preprocessed')
    dp.generate_preprocessed_documents()