class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n - 1
         
        max_container = 0
        while l < r:
            height = min(heights[l], heights[r])
            max_container = max(max_container, height * (r - l))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_container