# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:16:51 2020

@author: abhishek.sharma154
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    temp_dict = {}
    temp_list = []

    for x in strings:
        if x in temp_dict.keys():
            temp_dict[x] = temp_dict[x] +1
        else:
            temp_dict[x] =1
    
    print (temp_dict)
    for q in queries:
        temp_list.append(temp_dict[q])
    
    return temp_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()