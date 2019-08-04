sandwich_orders=["pastrami","fish","pastrami","fruit","beef","milk","pastrami"]
print("All the pastrami have been out.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print(sandwich_orders)