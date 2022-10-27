from xmlrpc.client import Boolean
from base_models.retrieval_model import RetrievalModel
from retrieval_models.boolean_model.boolean_query import BooleanQuery
from retrieval_models.boolean_model.boolean_document import BooleanDocument
from utils.preprocessor import Preprocessor
from utils.stack import Stack

class BooleanModel(RetrievalModel):
    """
        Class that represents a boolean model
    """

    def __init__(self, corpus):
        # get the corpus data
        super().__init__(corpus)

    def parse_query(self, query):
        return BooleanQuery(query)

    def parse_document(self, document):
        return BooleanDocument(document.text)

    def sim(self, document : BooleanDocument, query : BooleanQuery):
        """Evaluates the query against the corpus

        :param query_tokens: list of query tokens in postfix form
        :returns: list of matching document names
        """

        operands = Stack()

        for token in query.postfix_query:

            # Token is an operator,
            # Pop two elements from stack and apply it.
            if BooleanQuery.is_operator(token):
                # Pop right operand
                right_operand = operands.pop()

                # Pop left operand
                left_operand = operands.pop()
            
                # Perform operation
                result = self.perform_operation(left_operand, right_operand, token)

                # Push result back into the stack
                operands.push(result)

            # Token is an operand, push it to the stack
            else:
                # Lowercasing and stemming query term
                preprocessor = Preprocessor()
                token = preprocessor.st.stem(token.lower())

                # Push it's bit vector into operand stack
                operands.push( (not document.bit_vector[token]) if token[0] == '~' else document.bit_vector[token])

        if len(operands) != 1:
            print("Malformed query or postfix expression")
            return

        return operands.pop()

    def perform_operation(self, left, right, op):
        """Performs specified operation on the vectors

        :param left: left operand
        :param right: right operand
        :param op: operation to perform
        :returns: result of the operation
        """

        if op == "&":
            return left & right

        elif op == "|":
            return left | right

        else:
            return 0
