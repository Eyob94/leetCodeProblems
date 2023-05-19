class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        for i in tokens:
            if i not in operators:
                stack.append(i)
            else:
                ans = 0
                a = int(stack.pop())
                b = int(stack.pop())
                if i == '+':
                    ans = a + b
                elif i == '-':
                    ans = b-a
                elif i == '*':
                    ans = b*a
                else:
                    ans = b / a
                stack.append(ans)

        return int(stack.pop())

                   


