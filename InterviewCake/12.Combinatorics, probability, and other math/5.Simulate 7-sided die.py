# I do not clearly understand it

"""
Because rand5() has only 5 possible outcomes, and we need 7 possible results for rand7(),
we need to call rand5() at least twice.

When we call rand5() twice, we have 5∗5=25
5∗5=25 possible outcomes. If each of our 7 possible results has an equal chance of occurring, we'll need each outcome
to occur in our set of possible outcomes the same number of times.
So our total number of possible outcomes must be divisible by 7.

25 isn't evenly divisible by 7, but 21 is.
So when we get one of the last 4 possible outcomes, we throw it out and roll again.

So we roll twice and translate the result into a unique outcome_number in the range
1..25
1..25. If the outcome_number is greater than 21, we throw it out and re-roll. If not, we mod by 7 (and add 1).
"""


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
