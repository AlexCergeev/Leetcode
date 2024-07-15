class MinStack:

    def __init__(self):
        self.stack = []
        self.min_v = []

    def push(self, val: int) -> None:
        self.stack += [val]
        if len(self.stack) == 1:
            self.min_v += [val]
        else:
            self.min_v += [min(val, self.min_v[-1])]
        

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.min_v = self.min_v[:-1]
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_v[-1]
        
