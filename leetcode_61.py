# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        end = start = temp = head
        if head == None:
            return head

        cnt =0
        while True:
            cnt +=1
            if temp.next ==None:
                break
            temp = temp.next

        k = k % cnt
        x = cnt - k

        while x > 1:
            end = end.next
            x-=1

        temp.next = start
        new_start = end.next
        end.next = None

        return new_start
