class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_dict={}
        for num in nums:
            my_dict[num]=my_dict.get(num,0)+1
        
        for k,v in my_dict.items():
            if v>1:
                return True
        return False
        