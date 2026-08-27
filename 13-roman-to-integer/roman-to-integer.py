class Solution:
    def romanToInt(self, s: str) -> int:
        freq = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        num = 0
        n = len(s)
        for i in range(n):
            if i+1<n and freq[s[i]]<freq[s[i+1]]:
                num-=freq[s[i]]
            else:
                num+=freq[s[i]]
        return num