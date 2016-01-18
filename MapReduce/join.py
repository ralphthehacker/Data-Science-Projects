import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    # Input file = record[0]
    # Words in file = record[1]
    # Creating a key named after the file
    table_id = record[1]
    value = record
    # Emit the table id as the key and the entire row as the value
    mr.emit_intermediate(table_id,value)



def reducer(key, list_of_values):
    #Creating a data structure to store previous instances
    type_queue = []
    first_type = list_of_values[0][0]
    # Get the keys and form a new row based on the tables
    for data in list_of_values:
        if data[0] == first_type:
            type_queue.append(data)
        else:
            #making the output consistent, starting always with order
            for line in type_queue:
                if line[0] == 'order':
                    joined_row = line+data
                else:
                    joined_row = data+line
                #Emitting the joined row
                mr.emit((joined_row) )


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])

    mr.execute(data=inputdata, mapper=mapper, reducer=reducer)
