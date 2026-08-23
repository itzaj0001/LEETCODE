class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq={}
        for i,j in enumerate(nums):
            if j in freq:
                if abs(i-freq[j])<=k:
                    return True
                else:
                    freq[j] = i
            freq[j]=i
        return False
        