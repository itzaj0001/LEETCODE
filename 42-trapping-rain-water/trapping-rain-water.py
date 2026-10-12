class Solution:
    def trap(self, height: list[int]) -> int:
        water = 0 
        n = len(height)
        l, r = [0] * n, [0] * n

        l[0] = height[0]
        r[-1] = height[-1]

        for i in range(1,n):
            l[i] = max(height[i],l[i-1])

        for j in range(n-2,-1,-1):
            r[j] = max(height[j],r[j+1])
        
        for i in range(1,n-1):
            water += min(l[i],r[i]) - height[i]
        
        return water



        