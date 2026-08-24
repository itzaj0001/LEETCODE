class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        lst = sorted(nums)
        sum = 0
        for i in range(0,len(lst),2):
            sum += min(lst[i],lst[i+1])
        return sum
        