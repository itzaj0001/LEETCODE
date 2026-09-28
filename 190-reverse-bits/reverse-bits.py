class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(31,0,-1):
            res += (n & 1) << i
            n >>= 1

        return res
        