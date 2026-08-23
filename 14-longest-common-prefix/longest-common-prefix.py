class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)

        s = strs[0]

        for i in range(len(s), 0, -1):
            sub = s[:i]

            for j in strs:
                if not j.startswith(sub):
                    break
            else:
                return sub

        return ""

        
       
        