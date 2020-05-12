class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        if len(strs)==0:
            return ""
        prefix=""
        for i in range(len(strs[0])):
            count = 0
            for s in strs:
                if i<len(s) and strs[0][i] == s[i]:
                    count+=1
                    if count == len(strs):
                        prefix+=strs[0][i]
                else:
                    return prefix
        
        return prefix