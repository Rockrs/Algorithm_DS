class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        if high <12 or low>123456789:
            return []
        if low <12:
            low = 12
        if high >123456789:
            high = 123456789

        possibleNums = []
        for i in range(2, 10):
            for j in range(1, 10):
                temp = ""
                for k in range(j, 10):
                    temp += str(k)
                    if len(temp) ==i:
                        possibleNums.append(temp)
                        break

        i=0
        j = len(possibleNums)-1

        while True:
            if int(possibleNums[i]) >=low:
                break
            i+=1

        while True:
            if int(possibleNums[j]) <= high:
                break
            j-=1

        res = []
        while i<=j:
            res.append(int(possibleNums[i]))
            i +=1

        return res
