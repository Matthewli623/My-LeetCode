from collections import deque
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        d=deque(nums)
        
        for i in range(len(nums)):
            if len(d)!=0:
                temp = d.popleft()
                while temp==0 and d:
                    temp = d.popleft()
                nums[i]=temp
            else:
                nums[i]=0
                