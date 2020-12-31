class Solution:
    def sumSubseqWidths(self, arr: List[int]) -> int:
        mod = pow(10, 9) + 7
        n = len(arr)

        '''def fastexpo(a, b):
            res = 1
            while b>0:
                if b%2 ==1:
                    res = (res%mod * a%mod) %mod
                a = (a%mod * a%mod) %mod
                b = b//2
            return res'''

        res = 0
        arr.sort()

        x, y = 0, n-1
        for i in range(n):
            a = pow(2, x, mod)
            b = pow(2, y, mod)
            res = (res + (arr[i] * (a - b)) %mod) % mod
            x +=1
            y -=1

        return res
