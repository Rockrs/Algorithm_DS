import bisect
import math
class Solution:
    def smallestDivisor(self, arr: List[int], threshold: int) -> int:
        arr.sort()
        maxi =arr[-1]

        def b_search(i,j):
            print(i,j)
            if i==j:
                return i
            else:
                mid = i+(j-i)//2
                thres= bisect.bisect(arr,mid)
                k=thres

                for x in range(k,len(arr)):
                    thres += math.ceil(arr[x]/mid)
                if thres>threshold:
                    return b_search(mid+1,j)
                elif thres<=threshold:
                    return b_search(i,mid)

        return b_search(1,maxi)
