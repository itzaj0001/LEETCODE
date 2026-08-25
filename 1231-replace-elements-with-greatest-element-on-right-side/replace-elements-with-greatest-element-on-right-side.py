class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        if n == 1:
            return [-1]
        lst = [0]*n
        maxi = -1
        for i in range(n-1,-1,-1):
            lst[i] = maxi
            maxi = max(maxi,arr[i])
        return lst
            
            

        