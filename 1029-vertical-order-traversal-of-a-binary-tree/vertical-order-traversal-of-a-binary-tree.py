# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        def solve(node):
            lst = []
            q = deque([(node,0,0)])
            res = {}

            while q:
                e,row,col = q.popleft()
                if col in res:
                    res[col].append((e.val,row))
                else:
                    res[col] = [(e.val,row)]
                if e.left:
                    q.append((e.left,row+1,col-1))
                if e.right:
                    q.append((e.right,row+1,col+1))

            for value in sorted(res.items()): 
                node = value[1]
                node.sort(key=lambda x:(x[1],x[0]))
                lst.append([x[0] for x in node])
       
            return lst
            
        return solve(root)
        
        
            
            
                

                

                
            