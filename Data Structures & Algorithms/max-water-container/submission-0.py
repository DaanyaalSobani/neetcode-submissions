class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #O(n^2) solution
        max_volume =0
        for i,n in enumerate(heights):
            for j in range(i+1,len(heights)):
                volume = min(heights[i],heights[j]) * (j-i)
                max_volume = max(max_volume,volume)

        return max_volume