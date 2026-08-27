class Solution:
    def lowerBound(self,arr,target):
        lb = -1
        n = len(arr)
        low,high = 0, n-1
        while low<=high:
            mid = (low+high) //2
            if arr[mid] == target:
                lb = mid
                high = mid-1
            elif arr[mid]<target:
                low = mid+1
            else:
                high = mid -1
        return lb

    def upperBound(self,arr,target):
        up = -1
        n = len(arr)
        low,high = 0, n-1
        while low<=high:
            mid = (low+high) //2
            if arr[mid] == target:
                ub = mid
                low = mid+1
            elif arr[mid]>target:
                high = mid -1
            else:
                low = mid + 1
        return ub



    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lowerBound(nums,target)
        if lb == -1:
            return [-1,-1]
        ub = self.upperBound(nums,target)

        return [lb,ub]

        
        
        