class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) == 1:
            return [strs]

        d = dict()

        for i in strs:
            k = ''.join(sorted(i))
            if k in d:
                d[k].append(i)
            else:
                d[k] = [i] 
        
        return [d[x] for x in d]


        