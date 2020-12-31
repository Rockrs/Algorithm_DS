class Solution(object):
    def getMaximumGenerated(self, n):

        if n==0:
            return 0
        elif n==1:
            return 1

        arr=[0 for _ in range(n+1)]
        arr[0]=0
        arr[1]=1
        k = n//2
        if n%2==0:
            for i in range(1,k):
                a = i*2
                b = i*2 +1

                arr[a] = arr[i]
                arr[b] = arr[i]  +arr[i+1]
        else:
            for i in range(1,k+1):
                a = i*2
                b = i*2 +1

                arr[a] = arr[i]
                arr[b] = arr[i]  +arr[i+1]

        return max(arr)
