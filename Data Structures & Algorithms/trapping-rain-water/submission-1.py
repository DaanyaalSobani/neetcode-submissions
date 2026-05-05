class Solution:
    def trap(self, height: List[int]) -> int:
        x = {}
        for i,h in enumerate(height):
            max_left,max_right = 0,0
            for j,h_2 in enumerate(height):
                max_left = max(max_left,h_2) if j<i else max_left
                max_right = max(max_right,h_2) if j>i else max_right
                x[i] = {"max_left":max_left,"max_right":max_right,"height":h}
        res = 0
        for k,v in x.items():
            if v['height'] >= v['max_left'] or v['height'] >= v['max_right']:
                continue
            lower_height = min(v['max_left'],v['max_right'])
            diff = lower_height - v['height']
            res += diff
        return res
            