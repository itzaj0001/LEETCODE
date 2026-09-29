class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        lst = [0] * n
        st = []
          
        for i in range(n):
            while st and st[-1][0] < temperatures[i]:
                prev_temp, prev_index = st.pop()
                lst[prev_index] = i - prev_index

            st.append([temperatures[i], i])

        return lst