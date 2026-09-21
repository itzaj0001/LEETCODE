class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = dict()
        d2 = dict()

        for i, j in zip(s,t):
            if i not in d1:
                d1[i] = j
            if j not in d2:
                d2[j] = i

            if d1[i] != j or d2[j] != i:
                    return False
        return True



        