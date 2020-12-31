class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        for i in range(len(nums)-3,-1,-1):
            if i==len(nums)-3:
                nums[i]+= nums[i+2]
            else:
                nums[i]+= max(nums[i+2],nums[i+3])

        return max(nums)
