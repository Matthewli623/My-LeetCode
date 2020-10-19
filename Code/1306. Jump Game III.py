class Solution:
    def canReach(self, arr, start):
        endpt = {}
        for i in range(len(arr)):
            if arr[i] == 0:
                endpt[i] = 0
        visited = {}
        return self.helper(arr, start, endpt, visited)

    def helper(self, arr, i, endpt, visited):
        if i in visited or i < 0 or i >= len(arr) or i + arr[i] >= len(arr) or i - arr[i] < 0:
            return False
        if arr[i + arr[i]] == 0:
            return True
        else:
            visited[i] = False
            return self.helper(arr, i + arr[i], endpt, visited) or self.helper(arr, i - arr[i], endpt, visited)


s = Solution()
print(s.canReach([0, 3, 0, 6, 3, 3, 4], 6))
