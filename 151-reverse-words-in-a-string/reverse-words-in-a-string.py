class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        lst.reverse()
        s = ' '.join(lst)
        return s
        