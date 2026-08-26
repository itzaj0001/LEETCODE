class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        f0,f1 = 0,1
        for _ in range(n):
            f0,f1 = f1,f1+f0
        return f0
            

        