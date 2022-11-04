from utils.preprocessor import *

def run_preprocessing_test():
    # Initialize preprocessor
    preprocessor = Preprocessor("./datasets")

    # Get corpus documents
    corpus = preprocessor.generate_preprocessed_documents()

    # Print corpus length
    print(len(corpus))