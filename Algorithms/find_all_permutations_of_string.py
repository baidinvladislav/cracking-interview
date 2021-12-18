def permutations(str):
    if str == "":
        return [""]

    permutes = []
    for char in str:
        arg = str.replace(char, "", 1)
        subpermutes = permutations(arg)
        for each in subpermutes:
            permutes.append(char + each)
    return permutes


def main():
    print(permutations("abc"))


main()
