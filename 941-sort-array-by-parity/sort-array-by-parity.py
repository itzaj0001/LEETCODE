class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        lst = [0]*len(nums)
        even = 0
        odd = -1
        for i in nums:
            if i%2==0:
                lst[even] = i
                even +=1
            else:
                lst[odd] = i
                odd-=1
        return lst