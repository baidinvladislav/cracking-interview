# their bottom-up solution
# Time Complexity:
# Space Complexity:
def change_possibilities_bottom_up(amount, denominations):
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:

        for higher_amount in range(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += (
                ways_of_doing_n_cents[higher_amount_remainder]
            )

    return ways_of_doing_n_cents[amount]


# their memoization solution
# Time Complexity:
# Space Complexity:
class Change(object):

    def __init__(self):
        self.memo = {}

    def change_possibilities_top_down(self, amount_left, denominations, current_index=0):
        # Check our memo and short-circuit if we've already solved this one
        memo_key = str((amount_left, current_index))
        if memo_key in self.memo:
            print("grabbing memo[%s]" % memo_key)
            return self.memo[memo_key]

        # Base cases:
        # We hit the amount spot on. yes!
        if amount_left == 0:
            return 1

        # We overshot the amount left (used too many coins)
        if amount_left < 0:
            return 0

        # We're out of denominations
        if current_index == len(denominations):
            return 0

        print("checking ways to make %i with %s" % (
            amount_left,
            denominations[current_index:],
        ))

        # Choose a current coin
        current_coin = denominations[current_index]

        # See how many possibilities we can get
        # for each number of times to use current_coin
        num_possibilities = 0
        while amount_left >= 0:
            num_possibilities += self.change_possibilities_top_down(
                amount_left,
                denominations,
                current_index + 1,
            )
            amount_left -= current_coin

        # Save the answer in our memo so we don't compute it again
        self.memo[memo_key] = num_possibilities
        return num_possibilities


# their recursive solution
# Time Complexity:
# Space Complexity:
def change_possibilities_top_down(amount_left, denominations, current_index=0):
    # Base cases:
    # We hit the amount spot on. yes!
    if amount_left == 0:
        return 1

    # We overshot the amount left (used too many coins)
    if amount_left < 0:
        return 0

    # We're out of denominations
    if current_index == len(denominations):
        return 0

    print(f"checking ways to make {amount_left} with {denominations[current_index:]}")

    # Choose a current coin
    current_coin = denominations[current_index]

    # See how many possibilities we can get
    # for each number of times to use current_coin
    num_possibilities = 0
    while amount_left >= 0:
        num_possibilities += change_possibilities_top_down(
            amount_left,
            denominations,
            current_index + 1
        )
        amount_left -= current_coin

    return num_possibilities


change_possibilities_top_down(4, [1, 2, 3])
