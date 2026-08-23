class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        number = 0
        for i in nums:
            if count==0:
                number = i 
            if i == number:
                count+=1
            else:
                count-=1
        return number
        