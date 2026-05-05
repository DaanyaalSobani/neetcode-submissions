class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        max_left = [0] * n
        max_right = [0] * n

        # prefix: max up to and including i
        max_so_far = 0
        for i, h in enumerate(height):
            max_so_far = max(max_so_far, h)
            max_left[i] = max_so_far

        # suffix: max from i to end (including i)
        max_so_far = 0
        for i in range(n - 1, -1, -1):
            h = height[i]
            max_so_far = max(max_so_far, h)
            max_right[i] = max_so_far

        w = 0
        for l_h, r_h, h in zip(max_left, max_right, height):
            w += min(l_h, r_h) - h   # guaranteed >= 0 now

        return w
        