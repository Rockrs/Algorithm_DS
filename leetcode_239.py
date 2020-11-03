class Solution(object):
    def maxSlidingWindow(self, nums, k):

        arr =[]
        q = collections.deque()
        for i in range(k):

            while q and nums[i]>nums[q[-1]]:
                q.pop()
            q.append(i)
        arr.append(nums[q[0]])
        for i in range(k,len(nums)):
            #print(q,i)
            if i-q[0]==k:
                q.popleft()

            while q and nums[i]>nums[q[-1]]:
                q.pop()
            q.append(i)
            arr.append(nums[q[0]])
        return arr
