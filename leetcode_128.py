class Solution(object):
    def longestConsecutive(self, nums):
        if nums==[]:
            return 0
        d = set(nums)
        count = 1

        t=1
        while d:
            if min(d)+1 in d:
                t+=1
            else:
                count = max(t,count)
                t=1
            d.remove(min(d))

        return count
