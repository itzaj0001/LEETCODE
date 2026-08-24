class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        
        if r*c != row*col:
            return mat

        lst = []
        count = 1
        x = []
        for i in range(row):
            for j in range(col):
                if count>c:
                    lst.append(x)
                    count = 1
                    x = []
                if count<=c:
                    x.append(mat[i][j])
                    count+=1
        lst.append(x)
        return lst
                
                 
                



        