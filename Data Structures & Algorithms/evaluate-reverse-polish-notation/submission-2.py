class Node:
    def __init__(self, val, prev=None):
        self.val = val
        self.prev = prev

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        curr = None  # rightmost node so far
        
        for tok in tokens:
            if tok in "+-*/":
                # The two operands are the two nodes immediately behind curr
                r = int(curr.val)
                l = int(curr.prev.val)
                
                if tok == '+':
                    res = l + r
                elif tok == '-':
                    res = l - r
                elif tok == '*':
                    res = l * r
                else:
                    res = int(l / r)
                
                # Replace the two operand nodes with one result node
                curr = Node(str(res), prev=curr.prev.prev)
            else:
                # Just a number — append it
                curr = Node(tok, prev=curr)
        
        return int(curr.val)