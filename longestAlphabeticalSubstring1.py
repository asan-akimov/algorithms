# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:02:47 2023

@author: asan-akimov

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

"""


def las(s):
    temp = s[0]
    longest_substring = s[0]

    for i in range(len(s)-1):
        # print('i: ' + str(i))
        if s[i] <= s[i+1]:
            temp = temp+s[i+1]
            # print('  temp: ' + temp)
            if len(temp) > len(longest_substring):
                longest_substring = temp
                # print('  las: ' + longest_substring)
        else:
            temp = s[i+1]
            # print('  temp: ' + temp)

    return longest_substring


s1 = 'azcbobobegghakl'
s2 = 'abcbcd'
s3 = 'abcdefghijklmnopqrstuvwxyz'
s4 = 'gypijwnvcijk'

print(las(s1)) # beggh
print(las(s2)) # abc
print(las(s3)) # abcdefghijklmnopqrstuvwxyz
print(las(s4)) # cijk
