class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        st = []

        for i in tokens:
            if i in "+-*/":
                num2 = st.pop()
                num1 = st.pop()
                if i == "+":
                    st.append(num1 + num2)
                elif i == "-":
                    st.append(num1 - num2)
                elif i == "*":
                    st.append(num1 * num2)
                else:
                    st.append(int(num1 / num2))
            else:
                st.append(int(i))

        return st[-1]
                

        