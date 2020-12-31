class Solution:
    def averageWaitingTime(self, arr: List[List[int]]) -> float:
        waitingTime = 0
        finishTime = 0

        for i in range(len(arr)):
            x, y = arr[i]

            if i ==0:
                finishTime = x + y
                waitingTime += y
            elif x  >= finishTime:
                waitingTime += y
                finishTime = x + y
            else:
                waitingTime += finishTime - x + y
                finishTime += y

        return waitingTime/len(arr)
        
