class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        for i in range(n-2,-1,-1):
            if arr[i]==0:
                arr.pop()
                if i+1 == len(arr):
                    arr.append(0)
                    continue
                arr.insert(i+1,0)

        