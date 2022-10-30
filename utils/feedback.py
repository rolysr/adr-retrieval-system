import numpy as np

def classical_vector_feedback(documents_vectors, RR):
    """
        Return a classical vector feedback.
        This feedback can be used by any vector-based model
        for documents and queries
        Arguments:
        documents_vectors {list{np.array}} -- list of all document vectors that where recovered
        RR {int} -- number of relevant recovered documents
        Returns:
        np.array -- a new query vector that improves model's results
    """

    # result optimized query
    query_opt = np.zeros(len(documents_vectors[0]))
    RI = len(documents_vectors) - RR

    for doc_vector in documents_vectors:
        query_opt = query_opt + doc_vector*(1/RR) + doc_vector*(1/RI)

    return query_opt
    

def rocchio_algorithm(documents_vectors, q_zero, RR, alpha, beta, gamma):
    """
        Return a classical vector feedback.
        This feedback can be used by any vector-based model
        for documents and queries
        Arguments:
        documents_vectors {list{np.array}} -- list of all document vectors that where recovered
        RR {int} -- number of relevant recovered documents
        Returns:
        np.array -- a new query vector that improves model's results
    """

    # result optimized query
    query_opt = q_zero*alpha
    RI = len(documents_vectors) - RR

    for doc_vector in documents_vectors:
        query_opt = query_opt + doc_vector*(beta/RR) + doc_vector*(gamma/RI)

    return query_opt