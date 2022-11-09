import re

from base_models.document import Document
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
from collections import Counter

from utils.preprocessor import Preprocessor

class LinkParser(HTMLParser):
    """
        A class for parsing html files and get href tags
    """

    # adds links to a maintained list
    def handle_starttag(self, tag, attrs):
        """
            Add links to a maintained list
            Arguments
            tag {string} -- An html tag
            attrs {dict()} -- html attributes
        """
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href' and value.startswith("/") and value.find("css") == -1 and value.find("js") == -1:
                    newUrl = parse.urljoin(self.base_url, value)
                    self.links = self.links + [newUrl]

    # returns links
    def get_links(self, url):
        """
            Get the links from a given url
            Arguments:
            url {string} -- A string website url
            Returns:
            string -- The html string
        """
        self.links = []
        self.base_url = url

        response = urlopen(url)
        html_bytes = response.read()
        html_string = html_bytes.decode("utf-8")

        self.feed(html_string)
        return html_string, self.links

class Crawler:
    """
        A web crawler basic class for extracting data
        from a web url and return a group of documents
    """

    def __init__(self, website_url, max_pages) -> None:
        """
            Crawler constructor
            Arguments:
            website_url {string} -- Website url that will be analized
            max_pages {int} -- Max number of pages analized at most with this class
        """
        self.website_url = website_url
        self.max_pages = max_pages

    def remove_between(self, document, start_str, end_str):
        """
            Remove elements between documents from an start string to
            an end string
            Arguments:
            document {string} -- A document content
            start_str {string} -- Start string content
            end_str {strin} -- End string content
            Results:
            string -- Modified document string content
        """
        while start_str in document and end_str in document:
            start_str_index = document.find(start_str)
            end_str_index = document.find(end_str, start_str_index) + len(end_str) - 1
            document = document[0 : start_str_index] + document[end_str_index + 1 : len(document)]
        return document

    def get_documents(self):
        """
            Navigate through the specified url and get a list of documents
            Returns:
            list(document) -- List of documens created by using web data
        """
        pages_to_visit = [self.website_url]
        number_visited = 0
        documents = []

        while number_visited < self.max_pages and pages_to_visit != []:
            number_visited = number_visited +1

            url = pages_to_visit[0]
            pages_to_visit = pages_to_visit[1:]
            try:
                parser = LinkParser()
                data, links = parser.get_links(url)
                data = self.remove_between(data, "<script>", "</script>")
                data = self.remove_between(data, "<style>", "</style>")
                data = self.remove_between(data, "<", ">")

                words = re.sub("[^\w]", " ",  data)
                words = words.split()
                words = ' '.join(words)

                preprocessor = Preprocessor()
                preprocessor.tokenize(words)
                documents.append(Document(words, url))
                pages_to_visit = pages_to_visit + links
            except:
                print("Failed")

        return documents