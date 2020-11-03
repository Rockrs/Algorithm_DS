class Solution(object):
    def maxPower(self, s):

        maxi =1
        i=0
        while i<len(s):
            #print(i)
            local_max = 1
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    local_max +=1
                else:
                    break
            i+= local_max
            maxi = max(local_max,maxi)

        return maxi
