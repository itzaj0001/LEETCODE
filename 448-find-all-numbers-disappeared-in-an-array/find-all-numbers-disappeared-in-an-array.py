class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        lst = []
        n = len(nums)
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,0)+1
        for i in range(1,n+1):
            if i not in dic:
                lst.append(i)
        return lst

        
        
       
            

        