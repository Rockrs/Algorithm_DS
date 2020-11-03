class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        l1 =len(text1)
        l2 = len(text2)

        dp = [[0 for _ in range(l2)] for _ in range(l1)]

        def cal(i1,i2):
            if i1==l1 or i2==l2:
                return 0
            elif dp[i1][i2]!=0:
                return dp[i1][i2]
            elif text1[i1]==text2[i2]:
                dp[i1][i2] = 1 + cal(i1+1,i2+1)
                return dp[i1][i2]
            else:
                dp[i1][i2] = max(cal(i1+1,i2) , cal(i1,i2+1))
                return dp[i1][i2]

        return cal(0,0)
