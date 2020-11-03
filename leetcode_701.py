# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root==None:
            a =TreeNode()
            a.val =val
            return a
        else:
            t = root

            def insert_binary(t):
                if t.val>val:
                    if t.left==None:
                        t.left = TreeNode()
                        t.left.val = val
                        return
                    else:
                        insert_binary(t.left)
                        return
                elif t.val<val:
                    if t.right==None:
                        t.right=TreeNode()
                        t.right.val = val
                        return
                    else:
                        insert_binary(t.right)
                        return

            insert_binary(t)
            return root
