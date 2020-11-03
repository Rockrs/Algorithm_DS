#from collections import Counter
class Solution(object):
    def firstMissingPositive(self, nums):
        if nums==[]:
            return 1

        #nums = Counter(nums)
        ans =0
        l = len(nums)
        d= set()

        for i in range(1,l+2):
            d.add(i)

        for val in nums:
            d.discard(val)

        for i in range(1,l+2):
            if i in d:
                ans=i
                break
        return ans
        
