class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        if n!=m:
            return False
        
        freq = {}
        for i in s:
            freq[i] = freq.get(i,0) + 1
        for i in t:
            freq[i] = freq.get(i,0) - 1
            if freq[i] == -1:
                return False
        return True
        
        