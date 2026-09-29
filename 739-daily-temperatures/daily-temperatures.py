class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        days = [0] * n
        warmest = 1
        
        for i in range(n-1,-1,-1):
            temp = temperatures[i]

            if temp >= warmest:
                warmest = temp
                continue
            else:
                count = 1
                while True:
                    if temperatures[i + count] > temp:
                        days[i] = count
                        break
                    else:
                        count += days[i + count]

        return days