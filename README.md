# ADR Retrieval System
 ADR Retrival System is a full-stack information retrieval app developed with Python3 programming language. Its front-end was
 built with PyQt5 framework and QtDesigner desktop app. The backend was developed by using some useful Data Science tools from
 Anaconda framework such as Numpy and NLTK.
 
## Datasets

### Offline Datasets
 ---
 The offline datasets used for this project were [Cranfield](http://ir.dcs.gla.ac.uk/resources/test_collections/cran/), [Reuters-21578](https://archive.ics.uci.edu/ml/datasets/reuters-21578+text+categorization+collection) and [20-Newsgroups](http://qwone.com/~jason/20Newsgroups/), which are some of the most used datasets for tasks oriented to word processing, machine learning and information retrieval systems. A part of these repositories is stored in the [./datasets](https://github.com/rolysr/adr-retrieval-system/tree/main/datasets) folder where there are three folders, one for each dataset mentioned.
 
 ### Online Datasets
 ---
 Data sets from the Internet can be used thanks to the crawling methods implemented. It is only necessary to specify a seed url and a number of pages to be searched and the [crawler](https://github.com/rolysr/adr-retrieval-system/blob/main/utils/crawler.py) will return a document referring to the content of the pages analyzed.
 
 ## Requirements
  For the correct operation of the project, it is recommended to have the [Anaconda](https://www.anaconda.com/) framework installed, which includes the Numpy, Scipy and NLTK libraries.
  
  ### Main Dependencies to Install
   - Python 3.9+
   - Anaconda (which includes the main libraries)
   - Numpy
   - Scipy
   - uuid (A Python library for generating unique identifiers)
   - PyQt5 (Python library for front-end app to run)
All  those dependencies can be installed by using classic Python *pip* command.

### NLTK Data
Some of the funtionalities of this project such as [query expansion](https://github.com/rolysr/adr-retrieval-system/blob/main/utils/query_expansion.py) and [preprocessor](https://github.com/rolysr/adr-retrieval-system/blob/main/utils/preprocessor.py) need to have downloaded some important NLTK datasets that can be downloaded by the nexts commands on a terminal:

```bash
$ python3
>>> import nltk
>>> nltk.download('stopwords')
>>> nltk.download('wordnet')
>>> nltk.download('omw-1.4')
```

## How to Run the App

### Tests
To run the tests implemented in the [testing](https://github.com/rolysr/adr-retrieval-system/tree/main/testing) folder, it is only necessary to execute the run_tests.py script in the main folder of the project. It is also possible to add the tests that you want to test or create.
```bash
$ python3 run_tests.py
```

### Qt GUI
The Qt front-end base code is placed in [gui](https://github.com/rolysr/adr-retrieval-system/tree/main/gui) folder. In order to run the front-end you only need to use the following commands on a terminal:
```bash
$ python3 main.py
```

### Using the Models
This is a complete sample about how to use a model in a Python script:
```python
# Init preprocessor
preprocessor = Preprocessor('./datasets/cranfield')

# Get all corpus
corpus = preprocessor.generate_preprocessed_documents()

# Init boolean model
vsm = VectorSpaceModel(corpus)

# Make a query for a document
doc = corpus[0].text
query = "An experimental study of a wing in a propeller slipstream"

# Parse query and document
d = vsm.parse_document(doc)
q = vsm.parse_query(query)

s = vsm.sim(d, q)
print(s) # prints the similarity for the given query and document
```
The most recommended way to use the models is from the adr system which is a class that allows us to initialize several models at the same time with a given corpus and allows us to perform a series of basic queries.

```python
# Generate corpus
corpus = Preprocessor('./datasets/cranfield').generate_preprocessed_documents()

# Create instances of vector space model and boolean model
bm = BooleanModel(corpus)
vsm = VectorSpaceModel(corpus)
gvsm = GeneralizedVectorSpaceModel(corpus)

# Create an instance of ADR Retrieval System
adr = AdrRetrievalSystem(corpus, [bm, vsm,gvsm])

# Test basic query using vsm
query = "A wing is good"
query_response = adr.query(query, adr.models[1])

# Test basic query using bm
query = "wing | house | ( ~dog & wings )"
query_response = adr.query(query, adr.models[0])

# Test query by model name (vsm)
query = "A wing is good"
query_response = adr.query_model_name(query, "VectorSpaceModel")

# Test query k items on the response (vsm)
query = "A wing is good"
query_response = adr.k_documents_query_model(query, "VectorSpaceModel")

# Test query by model name (gvsm)
query = "A wing is good"
query_response = adr.query_model_name(query, "GeneralizedVectorSpaceModel")

# Test query k items on the response (gvsm)
query = "A wing is good"
query_response = adr.k_documents_query_model(query, "GeneralizedVectorSpaceModel")


print(query_response)
```
