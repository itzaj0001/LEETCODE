class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        
        if r*c != row*col:
            return mat

        lst = []
        current = []
        for i in range(row):
            for j in range(col):
                current.append(mat[i][j])

                if len(current)==c:
                    lst.append(current)
                    current=[]
        return lst

                
                 
                



        