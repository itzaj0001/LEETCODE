# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root:
            return root

        if root.val == key:
            return self.deletion(root)
        
        temp = root

        while temp:
            if temp.val > key:
                if temp.left and temp.left.val == key:
                    temp.left = self.deletion(temp.left)
                temp = temp.left
            else:
                if temp.right and temp.right.val == key:
                    temp.right = self.deletion(temp.right)
                temp = temp.right
        
        return root
    
    def deletion(self,node):
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        else:
            rightChild = node.right
            lastRightChild = self.findLastRight(node.left)
            lastRightChild.right = rightChild
            return node.left

    
    def findLastRight(self,node):
        while node.right:
            node = node.right
        return node


    
        