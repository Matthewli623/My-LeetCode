class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        sortedlist=sorted(intervals,key=lambda x:x[0])
        stack =[]
        for item in sortedlist:
            if stack and stack[-1][1]>=item[0]:
                temp=stack.pop()
                temp[1]=max(item[1],temp[1])
                stack.append(temp)
            else :
                stack.append(item)
                
        return stack
        