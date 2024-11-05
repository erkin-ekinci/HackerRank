# example the name "No Idea!"
"""There is an array of n integers. There are also 2 disjoint sets, A and B, each containing  integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if i is element of A, you add 1 to your happiness. If i is element of B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements."""

# # Enter your code here. Read input from STDIN. Print output to STDOUT
limits_n_m = list(map(int, input().split()))
whole = list(map(int, input().split()))
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

happiness = 0

for e in whole:
    if e in setA:
        happiness +=1
    elif e in setB:
        happiness -=1
        
print(happiness)