class Solution:
    def remove_duplicate(self, arr, N):

        k=1
        i=0
        j=1

        while(j<N):
            if arr[i]==arr[j]:
                j+=1
            elif arr[i]!=arr[j]:
                arr[i+1] = arr[j]
                i+=1
                j+=1
                k+=1
        return k

A = [1,1,1,2,2,2,3]
obj = Solution()
x = obj.remove_duplicate(A,len(A))
print (A)
