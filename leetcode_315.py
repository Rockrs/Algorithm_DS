from collections import defaultdict
class Solution(object):
    def countSmaller(self, nums):

        d =defaultdict(int)

        def merge(arr,l,r):

            mid = l + (r -l)//2

            i,j=l,mid+1
            temp=[]
            count=0
            while i<=mid and j<=r:
                if arr[j][0]<arr[i][0]:
                    temp.append(arr[j])
                    count+=1
                    j+=1
                else:
                    temp.append(arr[i])
                    d[arr[i]]+=count
                    i+=1
            while (i<=mid):
                temp.append(arr[i])
                d[arr[i]]+=count
                i+=1

            while j<=r:
                temp.append(arr[j])
                j+=1

            a=0
            for k in range(l,r+1):
                arr[k]=temp[a]
                a+=1

        def mergesort(arr,l,r):
            if l<r:
                mid = l + (r -l)//2
                mergesort(arr,l,mid)
                mergesort(arr,mid+1,r)
                merge(arr,l,r)

        B = [(nums[i],i) for i in range(len(nums))]
        mergesort(B,0,len(B)-1)

        res = [0 for i in range(len(nums))]
        for key,val in d.items():
            index = key[1]
            res[index]=val

        return res
