import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    # The matrix data is formatted as ['matrix name', 'row', column, value]
    # dna: The sequence itself
    matrix_name = record[0]
    row = record[1]
    column = record[2]
    value = record[3]
    # For every single value, I must emit it towards the cells where it will be used
    mr.emit_intermediate('dummy',record)


def reducer(key, list_of_values):
    # Receives intermediaries and processes them
    '''
    Logic necessary: Do matrix multiplication based on the dummy keys

    In real life, it would be necessary to emit keys for the final matrix's positions.
    The intermediary emitter is necessary to take advantage of parallellism, since it would be
    unlikely that all matrix data would fit in memory
    '''

    a_list = []
    b_list = []
    keys = {}
    #This code is awfully unoptimized
    for record in list_of_values:
        if record[0] == 'a':
            a_list.append(record)
        elif record[0] == 'b':
            b_list.append(record)

    # Now, emit the i,k,value position for C
    for a_value in a_list:
        for b_value in b_list:
            b_row = b_value[1]
            b_col = b_value[2]
            a_row = a_value[1]
            a_col = a_value[2]

            #Checking if A's row equals B's column
            if b_row == a_col:
                temp_key = (a_row,b_col)
                #Checking if this position has been seen before
                if temp_key not in keys.keys():
                    keys[temp_key] = a_value[3]*b_value[3]
                else:
                    keys[temp_key] = keys[temp_key] + a_value[3]*b_value[3]
    #Finally, emit the result
    for key in keys:
        mr.emit((key[0],key[1],keys[key]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(data=inputdata, mapper=mapper, reducer=reducer)
