class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        x1,x2 = rec1[0],rec1[2]
        y1,y2 = rec1[1],rec1[3] 

        x3,x4 = rec2[0],rec2[2]
        y3,y4 = rec2[1],rec2[3] 

        # ------------------------------------------------------

        # Method 1:
        # if x4 <= x1 or x3 >= x2 or y3 >= y2 or y4 <= y1:
        #     return False

        # return True

        # ------------------------------------------------------

        # Method 2:
        return min(x4,x2) > max(x1,x3) and min(y4,y2) > max(y1,y3)





        