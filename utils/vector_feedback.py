import numpy as np

def classical_vector_feedback(documents_vectors, RR):
    """
        Return a classical vector feedback.
        This feedback can be used by any vector-based model
        for documents and queries
        Arguments:
        documents_vectors {list{(np.array, bool)}} -- list of all document vectors that where recovered and a bool that indicates if its relvant or not
        RR {int} -- number of relevant recovered documents
        Returns:
        np.array -- a new query vector that improves model's results
    """

    # result optimized query
    query_opt = np.zeros(len(documents_vectors[0][0]))
    RI = len(documents_vectors) - RR

    for doc_vector, is_relevant in documents_vectors:
        query_opt = query_opt + (doc_vector*(1/RR) if is_relevant else doc_vector*(1/RI))

    return query_opt
    

def rocchio_algorithm(documents_vectors, q_zero, RR, alpha=1.0, beta=0.75, gamma=0.15):
    """
        Rocchio feedback.
        This feedback can be used by any vector-based model
        for documents and queries
        Arguments:
        documents_vectors {list{(np.array, bool)}} -- list of all document vectors that where recovered and a bool that indicates if its relvant or not
        q_zero {np.array} -- initial query vector
        alpha, beta, gamma {float} -- parameters for measure relevance of q_zero, RR and RI values
        RR {int} -- number of relevant recovered documents
        Returns:
        np.array -- a new query vector that improves model's results
    """

    # result optimized query
    query_opt = q_zero*alpha
    RI = len(documents_vectors) - RR

    for doc_vector, is_relevant in documents_vectors:
        query_opt = query_opt + (doc_vector*(beta/RR) if is_relevant else doc_vector*(gamma/RI)*(-1))

    return query_opt