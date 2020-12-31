# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        new_start = ListNode()
        new_start.next = head
        start = new_start

        while start !=None:
            while start.next != None and start.next.next != None and start.next.val == start.next.next.val:
                x = start.next
                y = start.next.val

                while x != None and x.val ==y:
                    x = x.next

                start.next = x

            start = start.next

        return new_start.next

        
