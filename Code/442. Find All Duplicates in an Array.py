class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d ={}
        res=[]
        for num in nums:
            if num in d:
                res.append(num)
            else :
                d[num]=1
        return res