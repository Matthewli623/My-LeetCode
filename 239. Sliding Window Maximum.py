class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if not nums:
            return nums
        ans=[]
        maxtemp=nums[0]
        for i in range(len(nums)-k+1):
            tempmax=nums[i]
            for j in range(i,i+k):
                tempmax=max(tempmax,nums[j])

            ans.append( tempmax)
            
        return ans