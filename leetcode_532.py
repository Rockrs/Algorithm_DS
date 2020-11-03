from collections import Counter
class Solution(object):
    def findPairs(self, nums, k):
        count =0
        a = Counter(nums)
        #print(a)
        for val in a:
            c = val-k
            if c in a:
                if c==val:
                    if a[c]>1:
                        count +=1
                else:
                    count += 1
        return count    
