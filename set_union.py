# Set .union() Operation
"""Task
The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper."""

# Enter your code here. Read input from STDIN. Print output to STDOUT
en_student_num = int(input())
en_set = set(map(int, (input().split(" "))))
fr_student_num = int(input())
fr_set = set(map(int, (input().split(" "))))

en_fr_set = set()

for en in en_set:
    for fr in fr_set:
        if en == fr:
            en_fr_set.add(en)
            continue

print(len(en_set) + len(fr_set) - len(en_fr_set))
            
