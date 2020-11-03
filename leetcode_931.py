class Solution(object):
    def minFallingPathSum(self, A):
        l  =len(A[0])

        dp = [[0 for _ in range(l)] for _ in range(l)]

        def cal(i,j):
            if dp[i][j]!=0:
                return dp[i][j]
            elif i+1==l:
                dp[i][j]= A[i][j]
                return A[i][j]
            elif j-1==-1:
                dp[i][j] = A[i][j] + min(cal(i+1,j),cal(i+1,j+1))
                return dp[i][j]
            elif j+1==l:
                dp[i][j] = A[i][j] + min(cal(i+1,j),cal(i+1,j-1))
                return dp[i][j]
            else:
                dp[i][j] = A[i][j] + min(cal(i+1,j-1),cal(i+1,j),cal(i+1,j+1))
                return dp[i][j]
            return

        for i in range(l):
            cal(0,i)
        #print (dp)
        return min(dp[0])
