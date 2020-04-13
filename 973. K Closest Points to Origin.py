
import math
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        d={}
        
        for pt in points:
            d[pt[0],pt[1]]=sqrt(pt[0]*pt[0]+pt[1]*pt[1])
            
            
        listd = sorted(d.items(),key=lambda x:x[1],reverse=False)
        

        ans=[]
        
        i=0
        diff=0
        pre=float("-inf")
        while diff<K:
            if listd[i][1]>=pre:
                pre=listd[i][1]
                ans.append([listd[i][0][0],listd[i][0][1]])
                diff+=1
            i+=1
    
        return ans