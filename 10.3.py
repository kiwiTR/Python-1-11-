file_name="guest.txt"
with open(file_name,"a") as file_object:
    while True:
        name = input("pleas input your name:")
        file_object.write(name+"\n")
        print("hello! "+name)
        symbol=input("do you want to continue?(yes/no)")
        if symbol=="no":
            break