goals={}
interview=True
while interview:
    name=input("Name?")
    goal=input("place?")
    goals[name]=goal
    repeat=input("Would you like to let another person respond?(yes/no)")
    if repeat=="no":
        interview=False
print(goals)