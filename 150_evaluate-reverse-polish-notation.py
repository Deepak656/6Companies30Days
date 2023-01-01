https://leetcode.com/problems/evaluate-reverse-polish-notation/
https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/869247944/
  
class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for c in tokens:
            a = 0
            b = 0
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]
