class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n =len(nums)
        nums.sort()
        closest = nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            j = i+1
            k = n-1
            while j<k:
                total = nums[i]+nums[j]+nums[k]
                if abs(closest-target)>abs(total-target):
                    closest = total
                if total<target:
                    j+=1
                else:
                    k-=1
        return closest

