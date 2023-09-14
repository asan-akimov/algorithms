# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:35:28 2023

@author: asan-akimov

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 

For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc

"""


def las(s):
    start = 0
    end = 0
    longest_start = 0
    longest_end = 0

    while end < len(s) - 1:
        # Move the end pointer one step.
        end += 1

        # If current character is not in alphabetical order with the previous one,
        # compare the current substring with the longest found so far.
        if s[end] < s[end - 1]:
            if end - start > longest_end - longest_start:
                longest_start, longest_end = start, end
            start = end

    # Handle the case where the longest substring is at the end.
    if end - start + 1 > longest_end - longest_start:
        longest_start, longest_end = start, end + 1

    return s[longest_start:longest_end]


s1 = 'azcbobobegghakl'
s2 = 'abcbcd'
s3 = 'abcdefghijklmnopqrstuvwxyz'
s4 = 'gypijwnvcijk'

print(las(s1)) # beggh
print(las(s2)) # abc
print(las(s3)) # abcdefghijklmnopqrstuvwxyz
print(las(s4)) # cijk
