class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        if len(coordinates) <=2:
            return True
        
        dx21 = coordinates[1][0] - coordinates[0][0]
        dy21 = coordinates[1][1] - coordinates[0][1]

        for i in range(2, len(coordinates)):
            dxi1 = coordinates[i][0] - coordinates[0][0]
            dyi1 = coordinates[i][1] - coordinates[0][1]

            if (dx21 * dyi1 != dy21 * dxi1):
                return False

        return True

        
        