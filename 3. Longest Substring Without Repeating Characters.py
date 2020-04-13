class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s :
            return 0
        res = 0
        seen=set("")
        for i in range(len(s)):
            j=i
            
            while j<len(s):
                if s[j] in seen:
                    res=max(len(seen),res)
                    seen.clear()
                    break 
                else :
                    seen.add(s[j])
                j+=1
                
            if(len(seen)>=len(s)-i):
                break

        return max(len(seen),res)
            