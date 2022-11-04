from utils.metrics import *

def run_metrics_tests():
    RR = 10
    REL = 50
    REC = 40
    RRD = 5

    print(precision(RR, REC))
    print(recall(RR, REL))
    print(r_precision(RR, REC, REL))
    print(f_score(RR, REL, REC))
    print(f_score(RR, REL, REC, Beta=1.5))
    print(response_time(120, 200))
    print(novelty_ratio(RRD, RR))