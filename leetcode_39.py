class Solution(object):
    def combinationSum(self, arr, target):

        ans = []

        def choices(A, i, k):
            if i == len(arr):
                return
            if k<0:
                return
            if k==0:
                ans.append(A)
                return

            choices (A, i+1, k) # Not Including Current Index
            choices (A+[arr[i]], i, k-arr[i])   # Including Current Index


        if arr:
            choices([], 0, target)
            return ans
        else:
            return ans

            
