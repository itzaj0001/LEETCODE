class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
    
        for i in asteroids:
            if i > 0:
                st.append(i)
            else:
                while len(st) != 0 and st[-1] > 0 and  abs(i) > st[-1]:
                    st.pop()
                if len(st) != 0 and abs(i) == st[-1]:
                    st.pop()
                elif len(st) == 0 or st[-1] < 0:
                    st.append(i)
        return st
        