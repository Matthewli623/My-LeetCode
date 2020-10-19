class Solution:
    def checkPerfectNumber(self, num):
        arr = []
        for i in range(1, num - 1):
            if num % i == 0:
                arr.append(i)

        if sum(arr) == num:
            return True
        else:
            return False


s = Solution()
print(s.checkPerfectNumber(28))
