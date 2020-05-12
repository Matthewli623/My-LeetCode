class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.s=[]
        
    def push(self, x: int) -> None:
        self.s.append(x)
        

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        if len(self.s)!=0:
            return self.s[-1]
        else:
            return 

    def getMin(self) -> int:
        mini=float("inf")
        for i in self.s:
            if mini>i:
                mini=i
        return mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()