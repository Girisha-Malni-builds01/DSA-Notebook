class Solution:
    def finalPrices(self, prices):
        n = len(prices)
        ans = prices[:]       # start with original prices
        stack = []            # will store indices

        for i in range(n):
            # Find next price <= current price
            while stack and prices[i] <= prices[stack[-1]]:
                idx = stack.pop()
                ans[idx] -= prices[i]  # apply discount
            stack.append(i)

        return ans
