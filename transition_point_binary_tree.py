# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:20:23 2020

@author: abhishek.sharma154
"""

def transition(arr,i,j):
    mid = int((j-i)/2)
    print (i,j)
    
    left = i+mid-1
    right = i+mid+1
    
    if arr[i+mid] ==1 and arr[left]==0:
        #print ("Hello")
        print (i+mid)
    
    if arr[i+mid] ==1 and arr[left]==1:
        transition(arr,i,left)
    
    if arr[i+mid]==0:
        transition(arr,right,j)
        

arr = [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]
transition(arr,0,len(arr)-1)


    