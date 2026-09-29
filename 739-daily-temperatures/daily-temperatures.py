class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        lst = [0]*n
        st = []

        for i in range(n):
            if len(st) == 0:
                st.append([temperatures[i],i])
            elif len(st) != 0 and st[-1][0] > temperatures[i]:
                st.append([temperatures[i],i])
            else:
                while len(st) != 0 and st[-1][0] < temperatures[i]:
                    lst[st[-1][1]] = i - st[-1][1]
                    st.pop()
                st.append([temperatures[i],i])
                
        return lst
