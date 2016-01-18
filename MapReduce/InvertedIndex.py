import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    # Input file = record[0]
    # Words in file = record[1]
    # Creating a key named after the file
    document_name = record[0]
    document_words = record[1]
    # And creating a dictionary to keep track of the repeated words
    repeated_words = []

    for word in document_words.split():
        if word not in repeated_words:
            mr.emit_intermediate(word,document_name)
            repeated_words.append(word)
        else:
            continue

def reducer(key, list_of_values):
    # Receives intermediaries and processes them
    # The reducer doesn't need to do anything besides returning the list of documents
    mr.emit((key,list_of_values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(data=inputdata, mapper=mapper, reducer=reducer)
