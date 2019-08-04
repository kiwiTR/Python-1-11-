print("Please input your age:")
message=True
while message:
    message=input()
    message=int(message)
    if message < 3 :
        print("Free to join.")
    else:
        if message < 12:
            money="10"
        else:
            money="12"
        print("You need to cost "+money+" .")
    break