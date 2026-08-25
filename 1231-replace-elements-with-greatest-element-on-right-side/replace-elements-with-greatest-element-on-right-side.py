class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        if n == 1:
            return [-1]
        lst = []
        maxi = -1
        for i in range(n-1,-1,-1):
            lst.append(maxi)
            maxi = max(maxi,arr[i])
        return lst[::-1]
            
            

        