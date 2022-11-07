import uuid

class Document:
    """
        Class that represents an abstract document
    """

    def __init__(self, text, url):
        """Receives a text as necessary data for a document.
        Arguments:
            text {string} -- document main content
        """
        self.id = uuid.uuid1()
        self.text = text
        self.url = url

    def __eq__(self, other):
        return self.id==other.id
    
    def __gt__(self, other):
        return self.id > other.id

    def __lt__(self, other):
        return self.id < other.id

    def __ge__(self, other):
        return self.id >= other.id

    def __le__(self, other):
        return self.id <= other.id

    def __str__(self) -> str:
        return self.id.int