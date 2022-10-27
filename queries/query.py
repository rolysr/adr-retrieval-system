class Query:
    """
        Class that represents an abstract query
    """

    def __init__(self, query):
        """
        Gets an instance of the corpus 
        Arguments:
            query {string} -- A string written by the user on an client-side app
        """    
        self.query = query 