import MapReduce
import sys

"""
Join Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # key1: friend pair
    # value: repeats
    key1 = record[0]
    key2 = record[1]
    mr.emit_intermediate((key1, key2), 1)
    mr.emit_intermediate((key2, key1), 1)


def reducer(key, repeats):
    # key: order id
    # value: list_of_records
    if len(repeats) == 1:
        mr.emit((key))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
