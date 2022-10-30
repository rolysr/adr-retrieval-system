from utils.crawler import Crawler

if __name__ == "__main__":
    c = Crawler("https://www.w3schools.com", 3)
    d = c.get_documents()
    for a in d:
        print('-----')
        print(a.text)