"""
Даны две строки, состоящие из строчных латинских букв. Требуется определить,
являются ли эти строки анаграммами, т. е. отличаются ли они только порядком следования символов.
"""
import sys


str1 = sys.stdin.readline()
str2 = sys.stdin.readline()


def is_anagram(str1, str2):
    arr = list(str2)

    for i in range(len(str1)):
        if str1[i] in arr:
            arr.remove(str1[i])

    if len(arr) == 0:
        return 1
    else:
        return 0


print(is_anagram(str1, str2))
