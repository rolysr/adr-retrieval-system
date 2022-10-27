from collections import Counter
from base_models.document import Document
import numpy as np

class BooleanDocument(Document):
    """
        Class that represents a boolean document
    """

    def __init__(self, text):
        # set main data from document
        super().__init__(text)

        # set data structure for document preprocessing
        self.bit_vector = self.gen_bit_vector(self.text)

    def get_bit_vector(self, document, vocab):
        """Make bitvector out of a document

        :param word: word
        :returns: bit vector of word with bits set when it appears in the particular documents
        """
        # create bit vector
        bit_vector = dict()

        # document words
        doc_words = list(set(document.split()))

        for word in vocab:
            bit_vector[word] = (word in doc_words)

        return bit_vector

        