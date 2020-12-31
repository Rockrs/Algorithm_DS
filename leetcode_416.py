class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2==1:
            return False

        n = len(nums)
        s = sum(nums)//2
        nums.sort()
        dp = {}

        def recur(i,j,k):
            if k==s:
                return True
            if k>s:
                return False
            if (i,k) in dp:
                return dp[(i,k)]
            else:
                res = False
                while(i<=j):
                    if recur(i+1,j,k+nums[i])==True:
                        dp[(i,nums[i]+k)], res= True, True
                        break
                    dp[(i,k+nums[i])] = False
                    i+=1
                dp[(i,k)] = res
                return dp[(i,k)]

        return recur(0,n-1,0)
