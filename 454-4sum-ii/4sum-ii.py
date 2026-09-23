class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        count = 0
        freq = dict()
        for i in nums1:
            for j in nums2:
                t = i + j
                if t in freq:
                    freq[t] += 1
                else:
                    freq[t] = 1

        for k in nums3:
            for l in nums4:
                s = k + l
                if -s in freq:
                    count += freq[-s]
                
        return count
        