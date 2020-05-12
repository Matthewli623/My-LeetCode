class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return 
        a=sorted(nums,reverse=True)
        return a[k-1]
