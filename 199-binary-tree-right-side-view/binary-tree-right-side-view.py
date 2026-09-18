# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        ans = []
        if not root:
            return ans
        q = deque([root])

        while q:
            level = len(q)
            for i in range(level):
                e = q.popleft()
                if i == level - 1 :
                    ans.append(e.val)
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
        return ans

        