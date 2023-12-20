class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        # Corner cases:
        #
        # Check if we have no money
        if money <= 0:
            return 0

        # Check if there is less than two chocolates in store
        if len(prices) < 2:
            return money

        # Actually we just need to buy two most cheap chocolates in store
        prices.sort()

        # Check if we do have enough money
        if prices[0] + prices[1] <= money:
            return money - (prices[0] + prices[1])
        else:
            return money
