class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        if len(nums)==0:
            return 0
        arr = []
        arr.append(1)
        for val in nums:
            arr.append(int(val))
        arr.append(1)

        n = len(arr)

        dp  = [[0 for j in range(n)] for i in range(n)]

        def max_s(i, j):
            if i==j==n:
                return 0
            elif i==j==0:
                return 0
            elif dp[i][j] !=0:
                return dp[i][j]
            else:

                max_ = float("-inf")
                k=i

                while k <= j:
                    if k-1 >= i:
                        dp[i][k-1] = max_s(i, k-1)
                    if k+1 <= j:
                        dp[k+1][j] = max_s(k+1, j)

                    temp_max = (arr[k] * arr[i-1] * arr[j+1]) + dp[i][k-1] + dp[k+1][j]
                    max_ = max(max_, temp_max)

                    k +=1

                dp[i][j] = max_
                return dp[i][j]

        return max_s(1, n-2)
