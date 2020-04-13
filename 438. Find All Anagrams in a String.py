class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s:
            return s
        i =0
        reslist=[]
        tarset=tuple(sorted(p))
        while i < len(s):
            if i+len(p)-1>len(s):
                break
            else :
                curs=s[i:i+len(p)]
                if tarset == tuple(sorted(curs)):
                    reslist.append(i)
            i=i+1
        
        return reslist