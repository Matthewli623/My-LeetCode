class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s=sorted(stones)
        while len(s)>1 :
            tempa = s.pop()
            tempb = s.pop()
            
            if tempa != tempb:
                s.append(tempa-tempb)
                s.sort()
        if len(s)==1:
            return s[0]
        else :
            return 0
