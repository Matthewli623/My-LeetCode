import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        c = collections.Counter(s)
        strbuilder=[]
        for val,feq in c.most_common():
            strbuilder.append(val*feq)
        return "".join(strbuilder)
            