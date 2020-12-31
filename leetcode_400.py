class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n

        # Idea is to Increaes val of cnt valriable till its greater than the Number
        # what does cnt variable do??
        # Basically it stores the count of digits from 1 to 99,999,9999,9999,..etc
        # Till 9,  total digit is 9 => cnt =9
        # Till 99, total digit is 2*90 +9 => cnt ==189
        # Till 999, total digit is 3*900 + 2*90 + 9 => cnt = 2889 and so on..
        # Now Suppose my cnt is 2889 and my Given Number is 4567
        # if we Substract cnt from 4567 then we know all numbers are of 4 digit because till 3 digits we have all Numbers in cnt
        # 4567 - 2889 = 1678, Now 1678//4 = 419 ... This tell us that we have 419 + 999 as our Number.
        # Rest is implementation and edge case
        # Hope You Like

        cnt =0
        i= 1

        while True:
            cnt += i * pow(10, i-1) * 9
            if cnt >=n:
                break
            i+=1

        cnt -= i * pow(10, i-1) * 9
        n -= cnt
        k, mod = divmod(n, i)


        Number = k + pow(10, i-1) -1

        if mod==0:
            return Number %10
        else:
            Number +=1
            x = str(Number)
            return int(x[mod-1])
