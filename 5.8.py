names=["admin","david","duke","mary","andy"]
if names:
    for name in names:
        if name =="admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello "+name+", thank you for logging in again")
else:
    print("We need to find some users!")

current_users=["admin","david","duke","mary","andy"]
new_users=["admin","tom","Duke","lily","huke"]
for user in new_users:
    if user.lower() in current_users:
        print("You need to use another name")
    else:
        print("You can use this name")

nums=list(range(1,10))
print(nums)
for num in nums:
    if num==1:
        print("1st")
    elif num==2:
        print("2nd")
    else:
        print(str(num)+"st")
