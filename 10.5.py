file_name="reasons.txt"
with open(file_name,"a") as file_object:
    while True:
        reason=input("why you like coding?\n")
        file_object.write(reason+"\n")
        signal=input("do you want to continue?(yes/no)")
        if signal=="no":
            break