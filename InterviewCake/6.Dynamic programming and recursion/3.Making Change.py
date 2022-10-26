# their bottom-up solution
# Time Complexity: O(n * m)
# Space Complexity: O(n)
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


# my code based on their memoization solution
# Time Complexity: O(n(amount_left) * m(len(denominations)))
# Space Complexity: O(n(amount_left) * m(len(denominations)))
def change_possibilities(amount_left, denominations, current_index=0, memo={}):
    if (amount_left, current_index) in memo:
        return memo[(amount_left, current_index)]

    if amount_left == 0:
        return 1

    if amount_left < 0:
        return 0

    if current_index == len(denominations):
        return 0

    combinations = 0
    current_coin = denominations[current_index]
    while amount_left >= 0:
        combinations += change_possibilities(amount_left, denominations, current_index + 1, memo)
        amount_left -= current_coin

    memo[(amount_left, current_index)] = combinations
    return combinations


# their recursive solution
# Time Complexity: O(n^^2)
# Space Complexity: O(n)
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
