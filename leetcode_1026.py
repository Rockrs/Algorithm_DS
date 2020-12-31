# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        ancestor_stk = []

        def traverse_t(s):
            if s==None:
                return float('-inf')
            else:
                ancestor_stk.append(s.val)
                a=traverse_t(s.left)
                b=traverse_t(s.right)
                x = ancestor_stk.pop()
                if ancestor_stk==[]:
                    return max(a,b)
                else:
                    return max(a,b,abs(x-max(ancestor_stk)),abs(x-min(ancestor_stk)))

        return traverse_t(root)
