# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def solve(self,node,p,q):
        curr = node
        while curr:
            if node.val > p.val and node.val > q.val :
                node = node.left
            elif node.val < p.val and node.val < q.val :
                node = node.right
            elif node == p or node == q:
                return node
            else:
                return node


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.solve(root,p,q)
        