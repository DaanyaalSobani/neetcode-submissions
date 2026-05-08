class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(sorted(zip(position,speed),reverse=True))
        stack = []
        fleet = 1
        for p,s in pair:
            stack.append((target - p)/s)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                fleet +=1
                stack.pop()
        return len(stack)
        