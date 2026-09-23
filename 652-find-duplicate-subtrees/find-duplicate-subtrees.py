# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicate(self,node,lst,d):
        if node == None:
            return ""

        k = "(" + self.findDuplicate(node.left,lst,d) +")" + str(node.val) + "(" + self.findDuplicate(node.right,lst,d) +")"

        d[k] = d.get(k,0) + 1

        if d[k] == 2:
            lst.append(node)

        return k


    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode | None]:
        lst = []
        d = {}
        self.findDuplicate(root,lst,d)
        return lst
        

    

        