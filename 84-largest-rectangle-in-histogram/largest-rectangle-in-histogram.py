class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        maxi = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                maxi = max(maxi, height * width)

            stack.append(i)

        heights.pop()
        return maxi