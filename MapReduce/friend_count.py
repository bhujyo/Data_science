import MapReduce
import sys

"""
Friend Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # key: friend A
    # value: friend B
    key = record[0]
    mr.emit_intermediate(key, 1)


def reducer(key, list_of_friends):
    # key: friend A
    # value: friends count
    count = 0
    for entry in list_of_friends:
        count += entry
    mr.emit((key, count))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
