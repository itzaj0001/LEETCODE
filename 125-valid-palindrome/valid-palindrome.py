class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = []
        
        if not s.strip():
            return True

        for i in s:
            if i.isalnum():
                lst.append(i.lower())
        
        n = len(lst)
        for i in range(n):
            if lst[i] != lst[n-i-1]:
                return False
        return True
        