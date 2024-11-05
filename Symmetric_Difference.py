# Symmetric Difference
"""Objective
Today, we're learning about a new data type: sets.
Concept
If the inputs are given on one line separated by a character (the delimiter), use split() to get the separate values in the form of a list. The delimiter is space (ascii 32) by default. To specify that comma is the delimiter, use string.split(','). For this challenge, and in general on HackerRank, space will be the delimiter."""

# Enter your code here. Read input from STDIN. Print output to STDOUT
M = input()
a = set(map(int, input().split()))
N = input()
b = set(map(int, input().split()))
# print(a)
# print(b)
# print(a^b)
# print(type(a^b))
# print(sorted(a^b))
[print(i) for i in sorted(a ^ b)]
