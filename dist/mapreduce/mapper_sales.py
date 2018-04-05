#!/usr/bin/python
#python 2.7
import sys

"""
This is a simple mapper that will ouput the store and the cost
of a sale. then this data will be output and sorted and finally
pass ove the reducer that will calculate the sales per store.
"""
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        data, time, store, item, cost, payment = data
        print("{0}\t{1}".format(store, cost) )
