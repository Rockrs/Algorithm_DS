from collections import deque
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        n = len(arr)
        arr.append(0)

        q = deque()
        t_max = float("inf")
        min_l = float("inf")
        j=0
        s = 0

        subarray_start  = [float("inf") for i in range(n)]
        subarray_end = [float("inf") for i in range(n)]

        for i in range(n):
            q.append(arr[i])
            s += arr[i]

            while s > target:
                s -= q.popleft()
                j+=1

            if s == target:
                subarray_start[j] = len(q)
                subarray_end[i] = len(q)

        for i in range(n):
            min_l = min(min_l, subarray_end[i])
            subarray_end[i] = min_l

        for i in range(1, n):
            if subarray_start[i] != float("inf"):
                if subarray_end[i-1] != float("inf"):
                    t_max = min(t_max, subarray_start[i] + subarray_end[i-1])

        if t_max == float("inf"):
            return -1
        else:
            return t_max
