import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    # sequence_id: The sequence which an ID comes from
    # dna: The sequence itself
    sequence_id = record[0]
    dna = record[1]
    # Removing the last 10 nucleotides
    dna = dna[:len(dna)-10]
    # Emitting the nucleotide sequence as akey alongside a dummy value
    mr.emit_intermediate(dna,1)

def reducer(key, list_of_values):
    # Receives intermediaries and processes them
    '''
    Logic necessary: Just emit the nucleotide sequence
    '''
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(data=inputdata, mapper=mapper, reducer=reducer)
