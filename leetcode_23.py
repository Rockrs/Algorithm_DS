# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        if lists==[]:
            return ListNode(val="")

        arr=[]
        for list in lists:
            s=list
            while s!=None:
                arr.append(s.val)
                s = s.next

        start=end=ListNode(val="")
        arr.sort()
        i=0
        while i<len(arr):
            if i==len(arr)-1:
                end.val=arr[i]
            else:
                end.val = arr[i]
                end.next = ListNode(val="")
                end = end.next

            i+=1
        return start
