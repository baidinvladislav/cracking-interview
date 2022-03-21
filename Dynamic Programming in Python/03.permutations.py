"""
Given a string, str, you are required to output an array containing all the possible permutations of that string.
By permutation, we simply mean all the different arrangements of the characters of that string.
"""


def permutations(str):
    if str == "":  # base case
        return [""]
    permutes = []
    for char in str:
        subpermutes = permutations(str.replace(char, "", 1))  # tabulation_fib step
        for each in subpermutes:
            permutes.append(char + each)
    return permutes


def main():
    print(permutations("abc"))


main()
