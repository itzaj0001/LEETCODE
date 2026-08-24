class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lst = []
        for i in nums:
            nums[abs(i) - 1] = -abs(nums[abs(i) - 1])
                
        
        for i in range(1,n+1):
            if nums[i-1]>0:
                lst.append(i)
        return lst

        
        
       
            

        