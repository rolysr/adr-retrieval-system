# Importing dependancy libraries
import os
import pandas as pd
import numpy as np
import re
import math as m
import nltk
from collections import Counter
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from documents.document import Document

# nltk.download('stopwords')

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
        self.stop_list = stopwords.words('english')
        
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

        # converting to string
        textData = ''.join(map(str, textData))
        # remove the SGML <tag> from text
        textData = textData.replace(tag, '')

        # calling function to generate tokens from text
        textData = self.tokenize(textData)

        return textData

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
                title = self.extractTokens(soup, 'title')

                # extract tokens for <text>
                text = self.extractTokens(soup, 'text')

                # create Document object
                document = Document(title + " " + text)

                # add document to the list of all documents
                documents.append(document)
            infile.close()

        return documents