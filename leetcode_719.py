class Solution:
    def smallestDistancePair(self, arr: List[int], k: int) -> int:

        arr.sort()
        n= len(arr)

        def count_n(mid):
            i=0
            j=1

            ans = 0
            while(j<n):
                while(i<j):
                    if abs(arr[j]-arr[i])<=mid:
                        break
                    i+=1
                ans += j-i
                j+=1
            return ans

        min_v = 0
        max_v = abs(arr[0]-arr[-1])
        for i in range(n-1):
            if abs(arr[i]-arr[i+1])<min_v:
                min_v = abs(arr[i]-arr[i+1])

        while(min_v!=max_v):
            mid = (min_v+max_v)//2
            res = count_n(mid)
            if res>=k:
                max_v = mid
            else:
                min_v = mid+1
        return min_v
