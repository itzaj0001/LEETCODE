class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        A = set(nums1)
        B = set(nums2)
        lst = list(A.intersection(B))
        return lst
            
                


        