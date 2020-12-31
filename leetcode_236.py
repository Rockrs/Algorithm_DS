# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def traverse_t(s,stk,node):
            if s==None:
                return 0
            if s.val==node.val:
                stk.append(node)
                return stk
            else:
                stk.append(s)
                a = traverse_t(s.left,stk,node)
                b = traverse_t(s.right,stk,node)

                if isinstance(a,list)==True or isinstance(b,list)==True:
                    return stk
                else:
                    stk.pop()
                    return 0

        p_anc = traverse_t(root,[],p)
        q_anc = traverse_t(root,[],q)
        l = min(len(p_anc),len(q_anc))
        ans =0

        for i in range(l):
            if p_anc[i].val==q_anc[i].val and i!=l-1:
                pass
            elif p_anc[i].val==q_anc[i].val and i==l-1:
                ans = p_anc[i]
                break
            elif p_anc[i].val!=q_anc[i].val:
                ans = p_anc[i-1]
                break

        return ans
