class Solution:
    def rob(self, nums: List[int]) -> int:

        currmax = 0
        premax=0
        for num in nums:
            temp =currmax
            currmax = max(premax+num,currmax)
            premax = temp
            
            
            
        return currmax