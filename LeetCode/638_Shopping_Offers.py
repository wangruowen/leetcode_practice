# https://leetcode.com/problems/shopping-offers/description/
class Solution(object):
    def __init__(self):
        self._price = None
        self._special = None
        self._num_items = 0
        self._min_total_price = 0

    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        # Iterate each offer and DFS with Backtracking search a list of offers that can cover all number of
        # items that need to buy.
        # DP: dp[needs] = min value for this needs
        self._price = price
        self._special = sorted(special, key=lambda x: (x[0], x[1]))
        self._num_items = len(price)
        self._min_total_price = sum(map(lambda x: x[0] * x[1], zip(price, needs)))
        self._helper(needs, [])

        return self._min_total_price

    def _helper(self, needs, used_offers):
        if sum(needs) == 0:
            # All items are purchased
            self._min_total_price = min(self._min_total_price, sum(x[-1] for x in used_offers))

        offer_matched = False
        for offer in self._special:
            valid = True
            rest = needs[:]
            for i in range(self._num_items):
                if offer[i] > needs[i]:
                    valid = False
                    break
                else:
                    rest[i] = needs[i] - offer[i]
            if valid:
                offer_matched = True
                used_offers.append(offer)
                self._helper(rest, used_offers)
                used_offers.pop()

        if not offer_matched:
            # No offer matched, we have to buy the original price
            cur_total = sum(x[-1] for x in used_offers)
            for i in range(self._num_items):
                cur_total += self._price[i] * needs[i]
            self._min_total_price = min(self._min_total_price, cur_total)


