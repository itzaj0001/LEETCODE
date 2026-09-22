class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row   = [set() for _ in range(9)]
        col   = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)] 

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == ".":
                    continue

                if cell in row[i]:
                    return False
                row[i].add(cell)

                if cell in col[j]:
                    return False
                col[j].add(cell)
                
                box = (3 * (i//3)) + (j//3)

                if cell in boxes[box]:
                    return False
                boxes[box].add(cell)
        return True

                
                


        
    
        