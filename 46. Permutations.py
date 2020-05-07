class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        resl = []
        self.helper(nums, resl, [], len(nums))
        return resl

    def helper(self, nums, resl, templ, length):
        if len(templ) == length:
            t = templ.copy()
            resl.append(t)
            return
        if nums == None:
            return
        for i in range(len(nums)):
            if nums[i] not in templ:
                templ.append(nums[i])
                self.helper(nums, resl, templ, length)
                templ.remove(nums[i])
        return

