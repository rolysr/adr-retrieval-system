class Document:
    """
        Class that represents an abstract document
    """

    def __init__(self, text):
        """Receives a text as necessary data for a document.
        Arguments:
            text {string} -- document main content
        """
        self.text = text