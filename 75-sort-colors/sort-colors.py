class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-1):
            mini = nums[i]
            minIndex = i
            for j in range(i+1,n):
                if nums[j] < mini:
                    mini = nums[j]
                    minIndex = j
            nums[i],nums[minIndex] = nums[minIndex],nums[i]

                