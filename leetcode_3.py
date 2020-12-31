class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        arr = [0 for i in range(301)]
        arr[0]=1

        g_max, i, j =0, 0, 0

        while (j<n):
            arr[ord(s[j])] +=1

            if arr[ord(s[j])] == 2:
                g_max = max(g_max, j-i)

                while arr[ord(s[j])] == 2:
                    arr[ord(s[i])] -=1
                    i +=1
            j +=1

        g_max = max(g_max,j-i)
        return g_max 
