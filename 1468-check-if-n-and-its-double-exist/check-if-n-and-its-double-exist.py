class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        mydict = {val:index for index,val in enumerate(arr)}
        
        for i in range(0,len(arr)):
            if 2*arr[i] in mydict and mydict[2*arr[i]]!=i:
                return True
        return False
        