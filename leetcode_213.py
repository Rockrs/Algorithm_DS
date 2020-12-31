class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        arr1  = nums[:-1]
        arr2  = nums[1:]

        for i in range(len(arr1)-3,-1,-1):
            if i ==len(arr1)-3:
                arr1[i]+= arr1[i+2]
            else:
                arr1[i]+= max(arr1[i+2],arr1[i+3])

        for i in range(len(arr2)-3,-1,-1):
            if i ==len(arr2)-3:
                arr2[i]+= arr2[i+2]
            else:
                arr2[i]+= max(arr2[i+2],arr2[i+3])

        return max(max(arr1),max(arr2))
