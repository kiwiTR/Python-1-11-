pizzas = ["fruit","meat","milk","egg"]
for pizza in pizzas:
    print(pizza+"\n")
    print("I like pepperoni pizza")
print("I really like pizza!")
print("\n")
print("The first three items in the list in the list are:")
print(pizzas[0:3])
print("Three items from the middle of the list are:")
print(pizzas[0:2])
print("The last three items in the list are:")
print(pizzas[1:4])
#下一个任务
friend_pizzas=pizzas[:]
pizzas.append("bird")
friend_pizzas.append("apple")
print("My favorite pizzas are:")
for my in pizzas:
    print(my)
print("My friend's favorite pizzas are:")
for friend in friend_pizzas:
    print(friend)
