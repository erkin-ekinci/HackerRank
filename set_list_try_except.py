# Set .discard(), .remove() & .pop()
"""Task
You have a non-empty set s, and you have to execute N commands given in N lines.
The commands will be pop, remove and discard.
NOTE: Try it in 'python 3' not in 'pypy 3' because the function of 'pop' command changed in those versions"""

n = int(input())
theList = set(map(int, (input().split(" "))))

command_number = int(input())

for _ in range(command_number):
    
    the_command = input().split(" ")
    
    if the_command[0] == "pop":        
        try:
            theList.pop()
        except KeyError:
            continue
            
    elif the_command[0] == "remove":
        try:
            theList.remove(int(the_command[1]))
        except KeyError:
            continue
            
    elif the_command[0] == "discard":
        try:
            theList.discard(int(the_command[1]))
        except KeyError:
            continue
            
    else:
        print("There is no that type of command")
        
print(sum(theList))