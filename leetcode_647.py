class Solution:
    def countSubstrings(self, arr: str) -> int:

        n = len(arr)

        dp = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            dp[i][i]  =1

        ans = 0
        for i in range(n-2, -1, -1):
            x = arr[i]
            for j in range(i+1, n):
                y = arr[j]
                if j == i+1 and x == y:
                    dp[i][j] = 1
                    ans +=1
                else:
                    if x == y and dp[i+1][j-1]!=0:
                        dp[i][j] = 1
                        ans +=1

        return ans + n
