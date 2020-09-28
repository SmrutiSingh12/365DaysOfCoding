#!/bin/python3
#Link:https://www.hackerrank.com/challenges/migratory-birds/problem
import math
import os
import random
import re
import sys
import collections

def migratoryBirds(arr):
    arr.sort()
    n1=collections.Counter(arr)

    i=max(n1.values())
    for key, value in n1.items(): 
         if i== value: 
             return key 
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
