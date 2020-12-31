# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, start: ListNode, k: int) -> ListNode:
        if k ==1:
            return start

        currptr = head = start
        finishptr, prevstart = None, None
        cnt  =0

        while head != None:
            cnt +=1
            if cnt % k ==0:
                finishptr = head
            head = head.next

        while currptr != finishptr:
            cnt = 0
            currstart = currptr
            prev = None

            while cnt < k:
                cnt += 1
                if cnt == k:
                    currend = currptr
                    if prevstart == None:
                        if currptr == finishptr:
                            start.next = currptr.next
                            currptr.next = prev
                            start = currptr
                            break
                        else:
                            prevstart = start
                            start = currend
                    else:
                        prevstart.next = currend
                        prevstart = currstart
                        if currptr == finishptr:
                            prevstart.next = currptr.next
                            currptr.next = prev
                            break


                temp = currptr.next
                currptr.next = prev
                prev = currptr
                currptr = temp

        return start
