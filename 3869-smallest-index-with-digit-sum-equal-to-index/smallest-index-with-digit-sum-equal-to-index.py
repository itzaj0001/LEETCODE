class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        index = -1
        for i in range(len(nums)):
            n = nums[i]
            s = 0
            while n > 0:
                d = n % 10
                n = n // 10
                s += d
            if s == i:
                index = i
                break
        return index

        