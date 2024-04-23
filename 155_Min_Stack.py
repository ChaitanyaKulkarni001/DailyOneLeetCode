# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.



class MinStack:

    def __init__(self):

        self.myStack  = []

    def push(self, val: int) :
        self.myStack.append(val)
        # print(self.myStack)

    def pop(self) :
        self.myStack = self.myStack[:-1]
        # print(self.myStack)

    def top(self) :
        # print(self.myStack)
        return self.myStack[-1]

    def getMin(self) -> int:
        # print(self.myStack)
        return min(self.myStack)
        


