from nltk.corpus import stopwords
from retrieval_models.boolean_model.boolean_model import BooleanModel

if __name__ == "__main__":
    p = [(1, 2), (2, 2), (1, 3)]
    p.sort()
    print(p)