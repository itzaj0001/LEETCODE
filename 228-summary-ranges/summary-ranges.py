class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n=len(nums)
        lst=[]
        if n==0:
            return lst
            
        s=nums[0]
        e=nums[0]
        
        for i in range(1,n):
            if e+1==nums[i]:
                e = nums[i]
            else:
                if s == e:
                    lst.append(f"{e}")
                    s = nums[i]
                    e = nums[i]
                else:
                    lst.append(f"{s}->{e}")
                    s = nums[i]
                    e = nums[i]
        if s == e:
            lst.append(f"{e}")
        else:
            lst.append(f"{s}->{e}")
            
        return lst
                
    