#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubarray function below.

def maxSubarray(arr,i,j):
    temp = []
    ### Temporary List
    for x in arr:
        temp.append(x)

    ### Maximum Subsequence
    max_sub =0
    for i in range(len(arr)):
        if arr[i]>0:
            max_sub += arr[i]
    if max_sub ==0:
        max_sub = max(arr)
    
    ### Maximum Cumulative Sum
    max_sum =0
    for i in range(len(temp)):
        if i >0:
            temp[i] += temp[i-1]
            if temp[i] > max_sum:
                print ("max sum")
                print (max_sum)
                max_sum = temp[i]

    ### Maximum Negative Cumulative Sum
    max_neg =0
    for i in range(len(temp)):
        if temp[i] < max_neg:
            max_neg = temp[i]
    
    if max_sum ==0:
        max_sum = max(arr)
    else:
        max_sum = max_sum - max_neg

    return max_sum , max_sub
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr,0,len(arr)-1)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()