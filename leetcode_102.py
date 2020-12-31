from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if root==None:
            return []

        level_d = defaultdict(list)
        ans = []

        def tree_t(s,level):
            if s==None:
                return
            else:
                level_d[level].append(s.val)
                tree_t(s.left,level+1)
                tree_t(s.right,level+1)

                return

        tree_t(root,0)
        maxi = max(level_d)

        for i in range(maxi+1):
            ans.append(level_d[i])
        return ans
