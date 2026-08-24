class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq ={i:0 for i in range(1,n+1)}
        for i in nums:
            freq[i]+=1

        for k,v in freq.items():
            if v==2:
                duplicate = k
            if v==0:
                missing = k
        return [duplicate,missing]

        