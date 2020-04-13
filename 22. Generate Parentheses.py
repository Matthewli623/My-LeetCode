class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n ==0:
            return []
        ans=[]
        stack=""
        l=n
        r=n
        self.helper(n,stack,0,0,ans)
        
        return ans
        
    def helper(self,n,s,l,r,ans):
        
        if r==n and l ==n:
            return ans.append(s)
        if l<n:
            self.helper(n,s+"(",l+1,r,ans)
        if r<l:
            self.helper(n,s+")",l,r+1,ans)
        