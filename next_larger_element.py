from collections import deque
def nextLargerElement(arr):
    q = deque()
    q.append(0)
    n = len(arr)

    index=1
    while(index<n):
        if arr[index]>arr[q[-1]]:
            while(len(q)!=0 and arr[index]>arr[q[-1]]):
                arr[q.pop()]= arr[index]
            q.append(index)
        elif arr[index]>arr[q[0]]:
            while(len(q)!=0 and arr[index]>arr[q[0]]):
                arr[q.popleft()] = arr[index]
            q.appendleft(index)
        else:
            q.appendleft(index)
        index+=1
    for i in range(len(q)):
        arr[q[i]]=-1

    return arr
