class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #all operators are binary 
        # we can store can track the left operand
        # whenever there's a operator we pop the two top elements
        stack = []
        for c in tokens:
            if c in ['+','-','*','/']:
                right_operand = int(stack.pop())
                left_opertand = int(stack.pop())
                if c == '+':
                    stack.append(left_opertand+right_operand)
                if c == '-':
                    stack.append(left_opertand-right_operand)
                if c == '*':
                    stack.append(left_opertand*right_operand)
                if c == '/':
                    stack.append(left_opertand/right_operand)
            else:    
                stack.append(c)
        return int(stack.pop())
        