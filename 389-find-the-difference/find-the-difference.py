class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mydict = {}
        for i in t:
            mydict[i] = mydict.get(i,0)+1
        for i in s:
            mydict[i] = mydict.get(i,0)-1
        for k,v in mydict.items():
            if v==1:
                return k



        