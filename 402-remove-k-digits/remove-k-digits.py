class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []

        for i in num:
            while st and st[-1] > i and k > 0:
                st.pop()
                k -=1

            if k == 0 or not st or st[-1] <= i:
                st.append(i)

        if k > 0:
            st = st[:-k] 
            
        return "".join(st).lstrip("0") or "0"
        