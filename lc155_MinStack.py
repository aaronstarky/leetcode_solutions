class MinStack:
    def __init__(self):
        self.mins = []
        self.stack = []      

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mins) != 0:
            self.mins.append(min(self.mins[-1], val))
        else:
            self.mins.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]

def test1():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    if minStack.getMin() != -3:
        return False
    minStack.pop()
    if minStack.top() != 0:
        return False
    if minStack.getMin() != -2:
        return False
    return True

print(test1())
    