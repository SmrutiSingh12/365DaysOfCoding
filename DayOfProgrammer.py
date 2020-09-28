#!/bin/python3
#https://www.hackerrank.com/challenges/day-of-the-programmer/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if (year == 1918):
        return '26.09.1918'
    elif year%4==0:
    
        if (year <= 1917  or (year > 1918 and  year%400 == 0  or year%100 != 0)):
           
            return "12.09.%s" %year
        else:
            return "13.09.%s" %year
    else:
        return "13.09.%s" %year
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(str(result) + '\n')

    fptr.close()
