class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack= []
        res = [0] * len(temperatures)
        for i,t in enumerate(temperatures):
            print(stack)
            while i and stack and t > stack[-1][1]:
                res[stack[-1][0]]=i-stack[-1][0]
                stack.pop()
            stack.append((i,t))
        print(stack)
        return res