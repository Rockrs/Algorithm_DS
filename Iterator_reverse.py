# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 11:31:06 2020

@author: abhishek.sharma154
"""

class Reverse:
    
    def __init__(self,list):
        self.list = list
        self.curr_index = len(self.list) -1
        #print (self.list is list)
        
    def __str__(self):
        #length = len(self.list)
        return "List is of {} object".format(self.curr_index)
    
    def __iter__(self):
        #print ("Calling Iter")
        return self
    
    def __next__(self):
        #print ("Calling Next")
        
        rev_num = self.list[self.curr_index]
        
        if self.curr_index >= 0:
            self.curr_index -= 1
        else:
            raise StopIteration
        
        return rev_num
        
a = [1,2,3,4,5,10,11,12,13]

for i in Reverse(a):
    print (i)
