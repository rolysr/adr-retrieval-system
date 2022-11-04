from utils.crawler import Crawler

def run_crawler_test():
    c = Crawler("https://www.w3schools.com/", 3)

    docs = c.get_documents()

    for i, doc in enumerate(docs):
        print("Doc {} has content:\n {}".format(i, doc.text))

