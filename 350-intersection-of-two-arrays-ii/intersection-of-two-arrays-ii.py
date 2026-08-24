class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        dic = {}
        lst = []

        if n<=m:
            for i in nums1:
                dic[i] = dic.get(i,0)+1
            
            for i in nums2:
                if i in dic and dic[i] != 0:
                    lst.append(i)
                    dic[i]-=1


        else:
            for i in nums2:
                dic[i] = dic.get(i,0)+1
            
            for i in nums1:
                if i in dic and dic[i] != 0:
                    lst.append(i)
                    dic[i]-=1

        return lst

        