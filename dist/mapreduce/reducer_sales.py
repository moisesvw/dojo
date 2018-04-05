#!/usr/bin/python
#python 2.7
import sys

"""
Reducer assumes that input is ordered by key. input is key\tvalue
the goal os to sum over the values of the keys
"""
total = 0
old_key = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # it is not expected format key \t value
        continue
    
    key, value = data_mapped

    if old_key and old_key != key:
        print("{0}\t{1}".format(old_key,total) )
        old_key = key
        total = 0

    old_key = key
    total += float(value)

if old_key != None:
    print("{0}\t{1}".format(old_key,total) )