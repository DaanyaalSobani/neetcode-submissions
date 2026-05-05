class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]*len(height)
        max_right = [0]*len(height)
        max_so_far = 0
        for i,h in enumerate(height):
            max_left[i]=max_so_far
            max_so_far = max(max_so_far,h)
        max_so_far = 0
        for i in range(len(height)-1,-1,-1):
            h = height[i]
            max_right[i]=max_so_far
            max_so_far = max(max_so_far,h)
        w=0
        for l_h,r_h,h in zip(max_left,max_right,height):
            print(l_h,r_h,h,max(min(l_h,r_h)-h,0))
            w+= max(min(l_h,r_h)-h,0)
        return w