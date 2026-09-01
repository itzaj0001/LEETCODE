class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
    
        for i in range(1,numRows):
            lst = [1]
            prev = res[-1]
            for j in range(1,i):
                lst.append(prev[j-1]+ prev[j])
            lst.append(1)
            res.append(lst)

        return res

        

        