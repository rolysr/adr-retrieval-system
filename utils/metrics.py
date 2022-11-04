# Objetive metrics
def precision(RR, REC):
    """
        Precision metric
        Arguments:
            RR {int} -- number of recovered relevant documents
            REC {int} -- number of recovered documents
        Returns
            Float -- Precision ratio
    """
    try:
        if REC==0:
            raise Exception()
        return RR/REC
    except (Exception):
        print("No recovered documents. Zero division.")

def recall(RR, REL):
    """
        Recall metric
        Arguments:
            RR {int} -- number of recovered relevant documents
            REL {int} -- number of relevant documents
        Returns
            Float -- Recall ratio
    """
    try:
        if REL==0:
            raise Exception()
        return RR/REL

    except (Exception):
        print("No relevant documents. Zero division.")

def f_score(RR, REL, REC, Beta=1):
    """
        F-score metric
        Arguments:
            RR {int} -- number of recovered relevant documents
            REC {int} -- number of recovered documents
            REL {int} -- number of relevant documents
            Beta {float} -- relevance for Precision or Recall
        Returns
            Float -- F-score
    """
    P = precision(RR, REC)
    R = recall(RR, REL)
    return ((1+ Beta**2)*P*R) / (Beta**2*P + R)

def r_precision(RR,REC,REL):
    """
        R-precision metric
        Arguments:
            RR {int} -- number of recovered relevant documents
            REC {int} -- number of recovered documents
            REL {int} -- number of relevant documents
        Returns
            Float -- R-precision
    """
    P = precision(RR, REC)
    R = recall(RR, REL)
    return P / R

# Subjetive metrics
def response_time(start_time, end_time):
    """
        Calculate time that need the system for a user response
        Arguments:
            start_time {float} -- time of query start
            end_time {int} -- time of query end
        Returns
            (Float, speed) -- Time elapsed in seconds and qualitative description of speed response
    """
    difference = end_time - start_time
    return (difference, 'Fast' if difference <= 1 else ('Normal' if 1 < difference <= 5 else 'Slow'))

def novelty_ratio(RRD, RR):
    """
        F-score metric
        Arguments:
            RRD {int} -- number of recovered relevant unknown documents
            RR {int} -- number of recovered relevant documents
        Returns
            Float -- Novelty ratio
    """
    return RRD / RR