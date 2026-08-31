class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        left = 0
        right = n-1
        i = n-1

        while left <= right:
            if abs(nums[left])<=abs(nums[right]):
                res[i] = abs(nums[right])**2
                right-=1
            else:
                res[i] = abs(nums[left])**2
                left+=1
            i-=1
        return res



        

        