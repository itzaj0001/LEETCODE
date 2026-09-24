class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1] and nums[i] > nums[i-1]:
                return i
        if nums[-1] > nums[-2]:
            return len(nums)-1
            
        