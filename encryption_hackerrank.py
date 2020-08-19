# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:25:17 2020

@author: abhishek.sharma154
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    string_list = []
    out_list = ""
    for x in s:
        if x !=" ":
            string_list.append(x)
    
    L = len(string_list)
    sq_root = math.sqrt(L)
    sq_floor = math.floor(sq_root)
    sq_ceil = math.ceil(sq_root)

    column =0
    item_pos = 0

    while(column < sq_ceil):
        while(item_pos<L):
            out_list = out_list + string_list[item_pos]
            item_pos = item_pos + sq_ceil
        out_list = out_list + " "
        column = column +1
        item_pos = column        
    
    #print (string_list)
    #print (string_list[0:8])
    #print (string_list[8:16])
    #print (string_list[16:23])
    #print (string_list[24:32])
    #print (string_list[32:40])
    #print (out_list)
    return out_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
