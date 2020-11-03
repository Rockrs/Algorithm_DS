class Solution(object):
    def shortestPalindrome(self, s):
        if s==s[::-1]:
            return s

        ans =""
        index=0
        for i in range(len(s)-1,1,-1):
            t = s[:i]
            if  t==t[::-1]:
                index=i
                #print(t)
                break

        if index==0:
            ans = s[:0:-1]+s
        else:
            ans = s[:index-1:-1] +s

        return ans
