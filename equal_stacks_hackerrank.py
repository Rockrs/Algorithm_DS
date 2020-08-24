#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #print (h1,h2,h3)
    h1.reverse()
    h2.reverse()
    h3.reverse()

    h1_height = sum(h1)
    h2_height = sum(h2)
    h3_height = sum(h3)
    res =0 

    if h1_height == h2_height == h3_height:
        res = h1_height
    else:
        smallest_max = min(h1_height,h2_height,h3_height)
        #print (f"Smallest height {smallest_max}")

        while len(h1)!=0 or len(h2)!=0 or len(h3)!=0:
            while(h1_height > smallest_max):
                h1_height -= h1[-1]
                h1.pop() 
            #print (f"h1 {h1} {h1_height}")
            while(h2_height > smallest_max):
                h2_height -= h2[-1]
                h2.pop()
            #print (f"h2 {h2} {h2_height}")
            while(h3_height > smallest_max):
                h3_height -= h3[-1]
                h3.pop()
            #print (f"h3 {h3} {h3_height}")

            if h1_height == h2_height == h3_height:
                res = h1_height
                break
            else:
                smallest_max = min(h1_height,h2_height,h3_height)
    return (res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()