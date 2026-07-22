class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minStack.pop()
        else:
            print("MinStack is empty")

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            print("MinStack is empty")
            return None

    def getMin(self) -> int:
        if self.stack:
           return self.minStack[-1]
        else:
            print("MinStack is empty")
            return None
            
