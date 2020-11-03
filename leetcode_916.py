from collections import Counter
class Solution(object):
    def wordSubsets(self, A, B):
        ans =[]

        ''' This is final Dictioanry containing freq of letters in B. Taking max of any specific character between two words'''
        d = {}

        ''' Procedure to take max of any specific characters between two words in B'''
        res  = True
        for char in B:
            b = Counter(char)

            '''Checking if freq of specific char in current_word is greater than freq of char in dict'''
            for key,val in b.items():
                if key not in d:
                    d[key] = val
                else:
                    d[key]   = max(val,d[key])

        ''' Checking for the Freq of characters in A and Final_dict d'''
        for word in A:
            a  = Counter(word)
            for key,val in d.items():
                if key not in a:
                    res = False
                    break
                elif a[key]<val:
                    res = False
                    break
            #print (res)
            if res:
                ans.append(word)
            res= True
        return ans
