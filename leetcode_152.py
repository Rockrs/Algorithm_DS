class Solution:
    def maxProduct(self, arr: List[int]) -> int:

        n = len(arr)
        curr_max = arr[0]
        curr_min  = arr[0]
        t_min = arr[0]

        for i in range(1, n):
            temp = curr_max

            curr_max = max(arr[i], arr[i] * curr_min, arr[i] * curr_max)
            curr_min = min(arr[i], arr[i] * curr_min, arr[i] * temp)

            t_min = max(t_min, curr_max)

        return t_min
