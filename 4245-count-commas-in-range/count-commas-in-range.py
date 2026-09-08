class Solution:
    def countCommas(self, n: int) -> int:
        if 1 <= n <= 999:
            return 0
        elif 1000 <= n <= 100000:
            comma = n - 999
            return comma
        

        
        