class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        num = abs(x)
        while num > 0:
            digit = num % 10
            res = res * 10 + digit
            num//=10
        if x < 0:
            res = -res
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res

        
