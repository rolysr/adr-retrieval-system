import os

"""
    This script was used to join many files from a dataset to just one file with all the content
"""

def joiner(in_path):
    cran = open(in_path + '/20newsgroups', 'w')
    filenames = os.listdir(in_path)
    
    for fname in filenames:
        # generate filenames
        infilepath = in_path + '/' + fname

        with open(infilepath) as infile:
            # read all text in a file
            fileData = infile.read()

            cran.writelines("<TITLE></TITLE>\n<TEXT>" + fileData + "</TEXT>\n")
        infile.close()
    cran.close()

if __name__ == "__main__":
    joiner('./datasets/20newsgroups')