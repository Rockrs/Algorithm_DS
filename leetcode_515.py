from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:

        out = []
        d = defaultdict(list)

        def traverse_t(head,l):
            if head is None:
                return
            else:
                d[l].append(head.val)
                traverse_t(head.left,l+1)
                traverse_t(head.right,l+1)
                return

        traverse_t(root,0)
        key=0
        while(key in d):
            out.append(max(d[key]))
            key+=1

        return out
