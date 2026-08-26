from math import sqrt
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        lst = []
        for i in range(1,int(sqrt(num))+1):
            if num%i == 0:
                lst.extend([i, num//i])
        return (sum(lst)-num)==num
        