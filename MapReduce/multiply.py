import MapReduce
import sys

"""
Multiply Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    if record[0] == 'a':
        for k in range(5):
            key = (record[1], k)
            value = (record[2], record[3])
            mr.emit_intermediate(key, value)
    else:
        for i in range(5):
            key = (i, record[2])
            value = (record[1], record[3])
            mr.emit_intermediate(key, value)


def reducer(key, value):
    count = 0
    for i in range(5):
        prod = []
        for item in value:
            if item[0] == i:
                prod.append(item[1])
        if len(prod) == 2:
            count += prod[0] * prod[1]
    mr.emit((key[0], key[1], count))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
