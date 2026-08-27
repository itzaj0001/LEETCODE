class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n == 1 or (n%2!=0):
            return False
        lst = []
        for i in range(n):
            if s[i] in "({[":
                lst.append(s[i])
                continue
            else:
                if len(lst)==0:
                    return False
                else:
                    if s[i] == ")":
                        if lst[-1] == "(":
                            lst.pop()
                            continue
                        else:
                            return False
                    if s[i] == "}":
                        if lst[-1] == "{":
                            lst.pop()
                            continue
                        else:
                            return False
                    if s[i] == "]":
                        if lst[-1] == "[":
                            lst.pop()
                            continue
                        else:
                            return False
        return len(lst)==0