from collections import Counter
class Solution(object):
    def findSubstring(self, s, words):
        w = len(words[0])
        W = len(words)
        res = []

        if len(s)< w*W:
            return []
        else:
            for i in range(len(s)):
                c = Counter(words)
                if i+W>len(s):
                    break
                k=i
                for _ in range(W):
                    char = s[k:k+w]
                    if c[char]!=0:
                        k+=w
                        c[char] -=1
                    elif c[char]==0:
                        break
                res.append(i)
                for val in c.values():
                    if val>0:
                        res.pop()
                        break
        return res
