import MapReduce
import sys

"""
Unique Trims Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    key = record[1][:len(record[1]) - 10]
    mr.emit_intermediate(key, record[0])


def reducer(key, list_of_values):
    mr.emit((key))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
