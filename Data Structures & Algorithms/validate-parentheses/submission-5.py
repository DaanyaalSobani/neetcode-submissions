class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {'(','[','{'}
        closing = {')',']','}'}
        for c in s:
            print(c)
            if c in opening:
                stack.append(c)
            if c in closing:
                if not stack:
                    return False
                last_bracket = stack.pop()
                if last_bracket == '(' and c != ')':
                    return False
                if last_bracket == '[' and c != ']':
                    return False
                if last_bracket == '{' and c != '}':
                    return False
        return len(stack) == 0
