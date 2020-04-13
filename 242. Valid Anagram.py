class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        if s>t:
            longs =s
            shorts= t
        else:
            longs =t
            shorts= s
        
        for i in longs:
            if i in d1:
                d1[i]=d1[i]+1
            else:
                d1[i]=1
        for j in shorts:
            if j in d2:
                d2[j]=d2[j]+1
            else:
                d2[j]=1
        
        for key,value in d1.items():
            if key not in d2:
                return False
            if d2[key] != value:
                return False
            
        
        return True