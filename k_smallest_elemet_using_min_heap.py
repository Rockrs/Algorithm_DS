# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 21:43:48 2020

@author: abhishek.sharma154
"""
def k_small(arr,k):
    for i in range(k):
       min_heapify(arr,0,len(arr)-1)
       k_min = arr[0]
       arr[0]= 1000000
      
    return k_min


def min_heapify(arr,i,N):
    parent = i
    left = 2*i +1
    right = 2*i +2
    
    #print (parent,left,right)
    if left ==N:
        if arr[left] < arr[parent]:
            temp = arr[parent]
            arr[parent] = arr[left]
            arr[left] = temp
        return
    
    elif left>N and right >N:
        return
    else:
        #print (parent,left,right)
        min_heapify(arr,left,N)
        if arr[left] < arr[parent]:
            temp = arr[parent]
            arr[parent] = arr[left]
            arr[left] = temp
        #print (arr)
        #print (parent,left,right)
        #print (arr[parent] )
        min_heapify(arr,right,N)
        if arr[right] < arr[parent]:
            temp = arr[parent]
            arr[parent] = arr[right]
            arr[right] = temp
    return (arr)

if __name__ == "__main__":
    
    arr = [765,8,6,0,12344,7,14,8,56565,654,9,0,123,65]
    
    #min = min_heapify(arr,0,len(arr)-1)
    k_min = k_small(arr,3)
    print (k_min)
    
    
    
    
    
    