class Solution:
    def __init__(self):
        self.d={0:0,1:1}
    
    def fib(self, n: int) -> int:
        if n in self.d:
            return self.d[n]
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        self.d[n]=self.fib(n-1)+self.fib(n-2)
        
        return self.d[n]