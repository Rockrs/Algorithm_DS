def maxSubarray(arr):
    ### Maximum Subsequence
    max_sub =0
    for i in range(len(arr)):
        if arr[i]>0:
            max_sub += arr[i]
    if max_sub ==0:
        max_sub = max(arr)
    #print (f"max_sub {max_sub}")

    max_s =0
    
    if all(item<0 for item in arr):
        print ("hello")
        max_s = max(arr)
    elif all(item>0 for item in arr):
        max_s = sum(arr)
    else:
        #print ("hi")
        temp =0
        for i in range(len(arr)):
            temp += arr[i]
            
            if temp <0:
                temp=0
            if temp> max_s:
                max_s = temp

    return (max_s,max_sub)