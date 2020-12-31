class Solution:
    def maxProfit(self, arr: List[int]) -> int:

        n = len(arr)
        ans = 0
        max_price = arr[n-1]

        for i in range(n-2,-1,-1):
            if arr[i] > arr[i+1]:
                ans += max_price - arr[i+1]
                max_price = arr[i]

        ans += max_price - arr[0]
        return ans
