class Solution(object):
    def countVowelStrings(self, n):
        arr = [5,4,3,2,1]
        if n==1:
            return 5
        elif  n==2:
            return 15
        else:
            for j in range(2,n):
                i=0
                while(i<5):
                    arr[i]=sum(arr[i:])
                    i+=1
        return sum(arr)
        
