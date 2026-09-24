# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        
        while low < high:
            mid = low + (high - low)//2

            cond = isBadVersion(mid)

            if cond:
                high = mid
            else:
                low = mid + 1
        
        if isBadVersion(low):
            return low
        else:
            return -1

