class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n = len(nums)
        largest = float("-inf")
        largest_index = -1
        
        for i in range(n):
            if nums[i] > largest:
                largest = nums[i]
                largest_index = i
        for i in range(n):
            if nums[i]*2 > largest and nums[i] != largest:
                return -1
        
        return largest_index

            




            


        