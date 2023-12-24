# container with most water
def maxArea(self, height: List[int]) -> int:
    max_a = 0
    l = 0
    r = len(height)-1
    while l < r:
        a = (r - l) * min(height[l], height[r])
        max_a = max(max_a, a)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_a