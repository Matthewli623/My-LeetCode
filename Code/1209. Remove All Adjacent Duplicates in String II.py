class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        if not s or s==" ":
            return s
        
        stack=[["#",0]]
        
        for c in s:
            if stack[-1][0]==c:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
                
                
            else :
                stack.append([c,1])
                
        strbuilder=[]
        for c , n in stack:
            strbuilder.append(c*n)
            
        return "".join(strbuilder)
        