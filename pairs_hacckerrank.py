# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:18:04 2020

@author: abhishek.sharma154
"""

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the pairs function below.
def pairs(k, arr):
    temp_list = []
    temp_dict = {}
    number =0
    for i in range(len(arr)):
        temp_list.append(arr[i]+k)
    
    for i in range(len(arr)):
        key = arr[i]
        temp_dict[key] = 1

    for j in range(len(temp_list)):
        key = temp_list[j]
        if key in temp_dict.keys():
            number = number +1
            #print (key)
    return number
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
