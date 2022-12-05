# their solution
# Time Complexity: O(inf)
# Space Complexity: O(1)
def rand7():
    while True:
        # Do our die rolls
        roll1 = rand5()
        roll2 = rand5()
        outcome_number = (roll1 - 1) * 5 + (roll2 - 1) + 1

        # If we hit an extraneous
        # outcome we just re-roll
        if outcome_number > 21:
            continue

        # Our outcome was fine. return it!
        return outcome_number % 7 + 1
