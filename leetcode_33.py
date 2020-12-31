class Solution:
    def search(self, arr: List[int], k: int) -> int:

        def pivot():
            ans=-1
            for i in range(len(arr)-1):
                if arr[i]>arr[i+1]:
                    ans = i
                    break
            return ans

        def b_search(temp,i,j):
            if i==j and temp[i]==k:
                return i
            if i==j and temp[i]!=k:
                return -1
            mid = i+(j-i)//2
            if temp[mid]==k:
                return mid
            elif temp[mid]<k:
                return b_search(temp,mid+1,j)
            elif temp[mid]>k:
                return b_search(temp,i,mid)

        x = pivot()
        if x==-1:
            return b_search(arr,0,len(arr)-1)
        else:
            temp = arr[x+1:]+arr[:x+1]
            y = b_search(temp,0,len(temp)-1)
            if y==-1:
                return -1
            else:
                if x+y>=len(arr)-1:
                    return (x+y)-(len(arr)-1)
                else:
                    return x+y+1
