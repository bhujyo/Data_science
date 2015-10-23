import MapReduce
import sys

"""
Join Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # key: order id
    # value: entry
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)


def reducer(key, list_of_records):
    # key: order id
    # value: list_of_records
    order = list_of_records[0]
    line_items = list_of_records[1:]
    for item in line_items:
        mr.emit((order + item))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
