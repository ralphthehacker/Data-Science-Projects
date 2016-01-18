import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    # user: Main person
    # friend: The friend
    user = record[0]
    friend = record[1]
    # The mapper will emit 2 records, first the user->friend record
    mr.emit_intermediate(user,friend)
    # Then the friend-> user record.
    mr.emit_intermediate(friend,user)

def reducer(key, list_of_values):
    # Receives intermediaries and processes them
    '''
    Since the mapper produces a pair of keys for every friend relationship, symmetrical friendships will have duplicates
    while asymmetric friendships will only have one record
    '''
    symmetric_friendships = []
    repeated_words = []
    for friend in list_of_values:
        if friend not in repeated_words:
            repeated_words.append(friend)
        else:
            symmetric_friendships.append(friend)
    # Repeating the for loop to emit the final result
    for friend in list_of_values:
        if friend not in symmetric_friendships:
            mr.emit((key,friend))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(data=inputdata, mapper=mapper, reducer=reducer)
