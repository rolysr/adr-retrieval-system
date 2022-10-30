from nltk.corpus import stopwords
from string import punctuation
from nltk import wordpunct_tokenize
from nltk.corpus import wordnet as wn

def query_expansion_by_synonyms(query):
    """
        Query expansion function that returns synonyms for 
        some words in the query string
        Arguments:
        query {string} -- query string that was used for a query
        Returns
        list(string) -- a list of words that can be used in a new
        query in order to get more specific documents in the response
    """

    english_stop = stopwords.words('english')
    all_stopwords = english_stop
    non_words = list(punctuation)
    
    non_words.extend(map(str, range(10)))
    tokens = wordpunct_tokenize(query)

    tokens = [elem for elem in tokens if (elem not in all_stopwords and elem not in non_words)]

    words=[]
    synonyms = []
    for token in tokens:
        print(token)
        for syn in wn.synsets(token):
            for lm in syn.lemmas():
                synonyms.append(lm.name())

        synonyms = (set(synonyms))
        words.extend(list(synonyms)[:2])
        synonyms = []

    return words
