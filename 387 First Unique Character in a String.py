class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        ch = {}
        for i in range(len(s)):
            if s[i] not in ch:
                ch.update({s[i]:1})
            else :
                value = ch.get(s[i])+1
                ch.update({s[i]:value})
        for i in range(len(s)):
            if ch[s[i]]==1:
                return i

                
        return -1