from collections import Counter
class Solution(object):
    def minDeletions(self, s):
        c = Counter(s)
        d = set()

        a=0

        for val in c.values():
            if val in d:
                removed = False
                for j in range(val-1,0,-1):
                    if j not in d:
                        a += val-j
                        removed =True
                        d.add(j)
                        break
                if removed==False:
                    a+=val
            else:
                d.add(val)

        return a
