#!/bin/python3
#problem Link: https://www.hackerrank.com/challenges/plus-minus/problem
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p=z=ng=0
    n=len(arr)
    
    for i in range(0,n):
        if arr[i]>0:
            p=p+1
        elif arr[i]==0:
            z=z+1
        else:
            ng=ng+1

   
    print("{:.6f}".format(p/n),"{:.6f}".format(ng/n),"{:.6f}".format(z/n),sep="\n")

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
