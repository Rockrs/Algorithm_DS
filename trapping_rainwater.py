def trappingWater(arr,n):

    left_max=[0 for _ in range(n)]
    right_max =[0 for _ in range(n)]
    l,r = float("-inf"),float("-inf")

    for i in range(n):
        if arr[i]>l:
            l=arr[i]
        left_max[i]=l

    for j in range(n-1,-1,-1):
        if arr[j]>r:
            r=arr[j]
        right_max[j]=r

    ans=0
    for i in range(1,n-1):
        ans += min(left_max[i],right_max[i])-arr[i]

    return ans
