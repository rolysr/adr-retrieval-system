# Importing dependancy libraries
import os
from sqlite3 import TimeFromTicks
from turtle import title
import pandas as pd
import numpy as np
import re
import math as m
import nltk
from collections import Counter
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from base_models.document import Document

# nltk.download('stopwords') # Uncomment this line in case you has not downloaded the stopwords from nltk
english_stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

class Preprocessor:
    """
        Class that represents a documents preprocessor object which tokenize, 
        parse and output the given documents from ./dataset 
    """

    # Init document preprocessor
    def __init__(self, in_path="./"):
        #The input and output data path
        self.in_path = in_path

        #stop list initialization
        self.stop_list = english_stopwords
        
        # Getting all filenames from the docs folder
        self.filenames = os.listdir(self.in_path)  # To generate file path

        # Initiallizing Porter Stemmer object
        self.st = PorterStemmer()

        # Initializing regex to remove words with one or two characters length
        self.shortword = re.compile(r'\W*\b\w{1,2}\b')
    
    
    def tokenize(self, data):
        """Preprocesses the string given as input. Converts to lower case,
        removes the punctuations and numbers, splits on whitespaces, 
        removes stopwords, performs stemming & removes words with one or 
        two characters length.
        Arguments:
            data {string} -- string to be tokenized
        Returns:
            string -- string of tokens generated
        """

        # converting to lower case
        lines = data.lower()

        # removing punctuations by using regular expression
        lines = re.sub('[^A-Za-z]+', ' ', lines)

        # splitting on whitespaces to generate tokens
        tokens = lines.split()

        # removing stop words from the tokens
        clean_tokens = [word for word in tokens if word not in self.stop_list]

        # stemming the tokens
        stem_tokens = [self.st.stem(word) for word in clean_tokens]

        # checking for stopwords again
        clean_stem_tokens = [word for word in stem_tokens if word not in self.stop_list]

        # converting list of tokens to string
        clean_stem_tokens = ' '.join(map(str,  clean_stem_tokens))

        # removing tokens with one or two characters length
        clean_stem_tokens = self.shortword.sub('', clean_stem_tokens)

        return clean_stem_tokens


    def extractTokens(self, beautSoup, tag):
        """Extract tokens of the text between a specific SGML <tag>. The function
        calls tokenize() function to generate tokens from the text.
        Arguments:
            beautSoup {bs4.BeautifulSoup} -- soup bs object formed using text of a file
            tag {string} -- target SGML <tag>
        Returns:
            string -- string of tokens extracted from text between the target SGML <tag>
        """

        # extract text of a particular SGML <tag>
        textData = beautSoup.findAll(tag)
        newTextData = []

        for tg in textData:
            # converting to string
            tg = ''.join(map(str, tg))
            
            # remove the SGML <tag> from text
            tg = tg.replace(tag, '')
            
            # calling function to generate tokens from text
            tg = self.tokenize(tg)

            newTextData.append(tg)

        return newTextData

    def generate_preprocessed_documents(self):
        """Returns a list of documents
        Returns:
            list(Document) -- list of documents
        """
        documents = list()

        for fname in self.filenames:
            # generate filenames
            infilepath = self.in_path + '/' + fname

            with open(infilepath) as infile:
                # read all text in a file
                fileData = infile.read()

                # creating BeautifulSoup object to extract text between SGML tags
                soup = BeautifulSoup(fileData, 'html.parser')

                # extract tokens for <title>
                titles = self.extractTokens(soup, 'title')

                # extract tokens for <text>
                texts = self.extractTokens(soup, 'text')

                # create Document objects
                for i in range(len(titles)):
                    document = Document(titles[i] + " " + texts[i], self.in_path)
                    
                    # add document to the list of all documents
                    documents.append(document)

                infile.close()

        return documents