class Solution:
    def jump(self, arr: List[int]) -> int:

        n = len(arr)
        if n==1:
            return 0
        jump =0
        i =0
        while i < n:
            maxSight = 0
            maxPos = i + arr[i]
            if i + arr[i] >= n-1:
                jump +=1
                break
            else:
                j = i+1
                while j <=maxPos:
                    if j + arr[j] > maxSight:
                        maxSight = j + arr[j]
                        i =j
                    j +=1
                jump +=1

        return jump
