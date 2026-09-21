class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        d = dict()

        for index,i in enumerate(list1):
            d[i] = index

        m = float("inf")

        for i,j in enumerate(list2):
            if j in d:
                index = i + d[j]
                if index < m:
                    lst = []
                    lst.append(j)
                    m = index
                elif index == m:
                    lst.append(j)
        return lst



        