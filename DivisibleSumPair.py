#!/bin/python3
#Problem Link:https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count=0
    for i in range(n-1):
        
        for j in range(i+1,n):
            if ar[i]+ar[j]==k or (ar[i]+ar[j])%k==0:
                count+=1
                print(ar[i],ar[j])

    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
