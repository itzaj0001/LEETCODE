class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk = []
        n = len(nums2)
        my_dict = {i:-1 for i in nums1}
        for i in range(n-1,-1,-1):
            while len(stk) != 0 and stk[-1] < nums2[i]:
                stk.pop()
            if len(stk) != 0 and stk[-1] > nums2[i] and (nums2[i] in my_dict):
                my_dict[nums2[i]] = stk[-1]

            stk.append(nums2[i])
        return [i for i in my_dict.values()]

        

    

        