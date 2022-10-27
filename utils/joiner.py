import os

def joiner(in_path):
    cran = open(in_path + '/cranfield', 'w')
    filenames = os.listdir(in_path)
    
    for fname in filenames:
        # generate filenames
        infilepath = in_path + '/' + fname

        with open(infilepath) as infile:
            # read all text in a file
            fileData = infile.read()

            cran.writelines(fileData)
        infile.close()
    cran.close()

if __name__ == "__main__":
    joiner('./dataset')