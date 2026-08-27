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
            if s[i]=="I"and i != n-1:
                if s[i+1] == "V" or s[i+1] == "X":
                    num-=1
                else:
                    num+=1
            elif s[i]=="X" and i != n-1:
                if s[i+1] == "L" or s[i+1] == "C":
                    num-=10
                else:
                    num+=10
            elif s[i]=="C" and i != n-1:
                if s[i+1] == "D" or s[i+1] == "M":
                    num-=100
                else:
                    num+=100
            else:
                num+=freq[s[i]]
        return num