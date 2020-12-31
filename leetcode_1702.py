class Solution:
    def maximumBinaryString(self, binary: str) -> str:

        n = len(binary)
        arr = [item for item in binary]
        firstZero = -1
        cnt = 0

        for i in range(n):
            if arr[i] =='0' and firstZero<0:
                firstZero = i
            elif arr[i] =='0':
                arr[i] = '1'
                cnt +=1

        if cnt < 1:
            return "".join(arr)
        else:
            arr[firstZero] = '1'
            arr[firstZero+cnt] = '0'
            return "".join(arr)
