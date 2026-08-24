class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lst = []
        for i in operations:
            if i =="+":
                if len(lst)>=2:
                    lst.append(lst[-1]+lst[-2])
            elif i=="C":
                if len(lst)>=1:
                    lst.pop()
            elif i=="D":
                if len(lst)>=1:
                    lst.append(2*lst[-1])
            else:
                lst.append(int(i))
        return sum(lst)



        