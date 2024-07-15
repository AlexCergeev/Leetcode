class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in {'+', '-', '*', '/'}:
                stack += [t]
            else:
                n2, n1 = stack.pop(), stack.pop()
                stack += [int(eval(f"{n1}{t}{n2}"))]
        return stack[-1]

