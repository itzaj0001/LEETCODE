class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)

        if k == n:
            return arr

        l  = 0 
        r = n - 1

        while l < r:
            m = l + (r - l) // 2

            if arr[m] >= x:
                r = m                 
            else:
                l = m + 1

        l = r - 1

        while k:
            if l < 0:
                r +=1
            elif r >= n:
                l-=1
            elif x - arr[l] <= arr[r] - x:
                l -= 1
            else:
                r+=1

            k-=1

        return arr[l+1:r]
        
    
        
  
        

        