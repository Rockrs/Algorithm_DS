class Solution:
    def stoneGame(self, arr: List[int]) -> bool:

        n = len(arr)

        dp = [[[0 for k in range(2)] for i in range(n)] for j in range(n)]

        for i in range(n):
            dp[i][i][1] = arr[i]
            dp[i][i][0] = 0

        for i in range(n-2, -1, -1):
            k = 1
            for j in range(i+1, n):
                if k==1:
                    x = arr[i] + dp[i+1][j][0]
                    y = arr[j] + dp[i][j-1][0]

                    if x >= y:
                        dp[i][j][0] = x
                        dp[i][j][1] = dp[i+1][j][1]
                    else:
                        dp[i][j][0] = y
                        dp[i][j][1] = dp[i][j-1][1]

                    k-=1
                elif k==0:
                    x = arr[i] + dp[i+1][j][1]
                    y = arr[j] + dp[i][j-1][1]

                    if x >= y:
                        dp[i][j][1] = x
                        dp[i][j][0] = dp[i+1][j][0]
                    else:
                        dp[i][j][1] = y
                        dp[i][j][0] = dp[i][j-1][0]

                    k += 1

        alex = dp[0][n-1][0]
        lee = dp[0][n-1][1]

        if alex > lee:
            return True
        else:
            return False
