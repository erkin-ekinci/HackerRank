# Nested Lists
"""Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line."""

if __name__ == '__main__':
    nestedList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nestedList.append([name, score])
    
    unique_scores = sorted(set([score for name,score in nestedList]))
    
    result = []
    for name, score in nestedList:
        if score == unique_scores[1]:
            result.append(name)
    result.sort()
     
    [print(x) for x in result]
    
