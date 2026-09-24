class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if k == n:
            return arr

        res = []
        l  = 0 
        r = n - 1

        while l < r:
            m = l + (r -l)//2
            if arr[m] >= x:
                r = m                 
            else:
                l = m + 1

        l = r - 1

        while k > 0:
            if l == -1:
                r +=1
            elif r == n:
                l-=1
            else:
                if abs(arr[l]-x) < abs(arr[r]-x):
                    l-=1
                elif abs(arr[l]-x) == abs(arr[r]-x):
                    if arr[l] < arr[r]:
                        l-=1
                    else:
                        r+=1
                else:
                    r+=1
            k-=1
        
        while l+1 < r:
            res.append(arr[l+1])
            l+=1
        return res

        


        
        

        