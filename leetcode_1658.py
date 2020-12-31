class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        if sum(nums)==x:
            return len(nums)

        maxi,t,n = float("-inf"),sum(nums)-x,len(nums)
        p_arr=[]
        d = {}

        p_arr.append(nums[0])
        for i in range(1,n):
            p_arr.append(nums[i]+p_arr[-1])

        for i in range(n):
            a = p_arr[i]-t
            if p_arr[i]==t:
                maxi = max(maxi,i+1)
            else:
                if a in d:
                    maxi = max(maxi,i-d[a])
            d[p_arr[i]]=i

        return -1 if maxi==float("-inf") else n-maxi
