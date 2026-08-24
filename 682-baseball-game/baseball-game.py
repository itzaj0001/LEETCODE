class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lst = []
        for i in operations:
            if i =="+":
                    lst.append(lst[-1]+lst[-2])
            elif i=="C":
                    lst.pop()
            elif i=="D":
                    lst.append(2*lst[-1])
            else:
                lst.append(int(i))
        return sum(lst)



        