class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        lst = [first]
        for i in encoded:
            lst.append(lst[-1]^i)
        return lst
        