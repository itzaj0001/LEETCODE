class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = x ^ y
        return ans.bit_count()
        # count = 0

        # for i in range(0,32):

        #     if ans &(1<<i)!=0:
        #         count+=1

        # return count
        