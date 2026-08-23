from math import ceil
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        max = ceil(n/2)
        hashmap ={}

        for i in nums:
            hashmap[i] = hashmap.get(i,0)+1

        for k,v in hashmap.items():
            if v>=max:
                return k
        