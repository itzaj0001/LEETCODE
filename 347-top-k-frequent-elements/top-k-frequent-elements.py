class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        freq = sorted(freq.items(),key=lambda x:x[1],reverse=True)
        return [x[0] for x in freq[:k]]

        