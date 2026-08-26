class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n =len(nums)
        nums.sort()
        closest = float("inf")
        for i in range(n-2):
            j = i+1
            k = n-1
            while j<k:
                total = nums[i]+nums[j]+nums[k]
                diff = abs(total-target)
                if diff<closest:
                    closest = diff
                    temp = [i,j,k]
                if total<target:
                    j+=1
                else:
                    k-=1
        return nums[temp[0]]+nums[temp[1]]+nums[temp[2]]

