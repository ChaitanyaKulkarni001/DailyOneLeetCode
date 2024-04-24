class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ['+','-','*','/']
        stack = []

        for i in tokens:
            if i not in operands:
                stack.append(i)
            else:
                b = int(stack.pop(-1))
                a = int(stack.pop(-1))
                # print("A =",a)
                # print("B =",b)
                if i == '+':
                    stack.append(a+b)
                    # print(stack[-1])
                    # print(stack)
                elif i == '-':
                    stack.append(a-b)
                    # print(stack[-1])
                    # print(stack)
                elif i == '*':
                    stack.append(a*b)
                    # print(stack[-1])
                    # print(stack)
                    # print(stack)
                else:
                    stack.append(a/b)
                    # print(stack[-1])
                    # print(stack)

        return int(stack[0])
