class Solution(object):
    def findUnsortedSubarray(self, nums):
        arr = [item for item in nums]
        nums.sort()
        l,r = 0,0

        for i in range(len(arr)):
            if arr[i]!=nums[i]:
                l=i
                break

        for j in range(len(arr)-1,-1,-1):
            if arr[j]!=nums[j]:
                r=j
                break

        if l==0 and r==0:
            return 0
        else:
            return r-l+1 
