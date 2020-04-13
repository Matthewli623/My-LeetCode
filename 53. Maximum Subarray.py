class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if max(nums)<0:
            return max(nums)
        
        resmax=0
        tempmax=0
        
        for num in nums:
            tempmax=max(0,num+tempmax)
            resmax=max(tempmax,resmax)
            
                
        return resmax
                
        