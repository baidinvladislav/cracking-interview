def countChar(str, char):
    '''
    you can call helper function as countChar_(str[1:], char)
    '''
    if len(str) <= 0:
        return 0
    if str[0] == char:
        return 1 + countChar(str[1:], char)
    else:
        return countChar(str[1:], char)


print(countChar("abacada", 'a'))
