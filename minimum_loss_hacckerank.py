#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Complete the minimumLoss function below.
def minimumLoss(price):
    temp_list = copy.copy(price)
    temp_list.sort()

    min = temp_list[1] - temp_list[0]
    for i in range(len(price)-1):
        if (temp_list[i+1]-temp_list[i] <min):
            #print (price.index(temp_list[i]))
            #print (price.index(temp_list[i+1]))
            if price.index(temp_list[i]) > price.index(temp_list[i+1]):
                min = temp_list[i+1] - temp_list[i]
                #print (min)
    return min

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
