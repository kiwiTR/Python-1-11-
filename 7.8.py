sandwich_orders=["fish","meat","fruit","beef","milk"]
finished_sandwiches=[]
while sandwich_orders :
    sandwich=sandwich_orders.pop()
    print("I made your "+sandwich+" sandwich.")
    finished_sandwiches.append(sandwich)
print("All the sandwich have been finished.")
print(finished_sandwiches)