class Solution(object):
    def maxPower(self, s):

        dp =[[1 for _ in range(len(s))]for _ in range(len(s))]

        for i in range(len(s)-2,-1,-1):
            for j in range(i+1,len(s)):
                if j==len(s)-1:
                    t = s[i:]
                    if all(item==t[0] for item in t):
                        dp[i][j] = len(t)
                    else:
                        dp[i][j] =max(dp[i][j-1],dp[i+1][j])
                else:
                    t = s[i:j+1]
                    if all(item==t[0] for item in t):
                        dp[i][j] = len(t)
                    else:
                        dp[i][j] = max(dp[i][j-1],dp[i+1][j])

        return dp[0][len(s)-1]
