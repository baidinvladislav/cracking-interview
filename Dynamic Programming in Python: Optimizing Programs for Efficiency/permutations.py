def permutations(str):
    if str == "":  # base case
        return [""]
    permutes = []
    for char in str:
        subpermutes = permutations(str.replace(char, "", 1))  # recursive step
        for each in subpermutes:
            permutes.append(char + each)
    return permutes
