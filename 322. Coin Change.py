class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [2**31 - 1] * (amount+1) 
        f[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
        # f[i] = current no possilbe combination which done by pre coins
        # f[i-coin] + 1 = (current amount - coin amount) in no possilbe combination- + current coin
                f[i] = min(f[i], f[i-coin] + 1)
        if f[amount] == 2**31 - 1:
            return -1
        return f[amount]