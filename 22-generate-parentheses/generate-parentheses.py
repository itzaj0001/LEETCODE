class Solution:
    def solve(self,index,total,brackets,res):
        if index >= len(brackets):
            if total == 0:
                res.append("".join(brackets))
            return 

        if total < 0:
            return 

        if total > len(brackets) // 2:
            return 

        brackets[index] = '('
        self.solve(index+1,total+1,brackets,res)

        brackets[index] = ')'
        self.solve(index+1,total-1,brackets,res)
            

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        brackets = ['']*(n*2)
        self.solve(0,0,brackets,res)
        return res

       