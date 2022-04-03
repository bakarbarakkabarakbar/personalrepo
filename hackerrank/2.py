#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxElement' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER maxSum
#  3. INTEGER k
#
from numpy import zeros

def maxElement(n, maxSum, k):
    valuek = 0
    differential = maxSum #differentialbetweenmaxsumandcurrentsum
    while differential > 0:
        valuek += 1
        differential -= 1 
        if differential <= 0:
            break
        if (maxSum - n) == 0:
            return valuek
        
        indexposition = k #indexpositionrelativetoarrayindex
        indexlength = 1 #howfarbetweenindexpositionarelativetok
        indexlengthposition = 0 
        
        while (indexposition > 0) and (indexlengthposition < indexlength):
            indexposition -= 1
            indexlengthposition += 1
            differential -= 1 
            if differential <= 0:
                break
            
            
        
        indexposition = k
        indexlengthposition = 0
        while (indexposition < n-1) and (indexlengthposition < indexlength):
            indexposition += 1
            indexlengthposition += 1
            differential -= 1 
            if differential <= 0:
                break
            
                
        if indexlength >= k or indexlength >= (n-k):
            continue
        else:   
            indexlength += 1
            
    return int(valuek)
    # Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    maxSum = int(input().strip())

    k = int(input().strip())

    result = maxElement(n, maxSum, k)

    fptr.write(str(result) + '\n')

    fptr.close()
