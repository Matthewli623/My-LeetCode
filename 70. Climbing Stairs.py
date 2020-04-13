class Solution:
    
    def __init__(self):
        self.d={0:0,1:1,2:2}
        
        
    def climbStairs(self, n: int) -> int:
        
        if n in self.d:
            return self.d[n]
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        self.d[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        
        return self.d[n]