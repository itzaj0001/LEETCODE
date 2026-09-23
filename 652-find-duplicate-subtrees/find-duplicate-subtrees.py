# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicate(self, node, lst, d, ids):
        if node is None:
            return 0

        left = self.findDuplicate(node.left, lst, d, ids)
        right = self.findDuplicate(node.right, lst, d, ids)

        key = (left, node.val, right)

        if key not in ids:
            ids[key] = len(ids) + 1

        curr_id = ids[key]

        d[curr_id] = d.get(curr_id, 0) + 1

        if d[curr_id] == 2:
            lst.append(node)

        return curr_id


    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode | None]:
        lst = []
        d = {}
        ids = {}

        self.findDuplicate(root, lst, d, ids)
        return lst
        

    

        