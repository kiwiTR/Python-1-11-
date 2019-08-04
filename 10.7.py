print("please input two numbers and I will add them.")
while True:
    num1=input("the first:")
    num2=input("the second:")
    try:
        result=int(num1)+int(num2)
    except ValueError:
        print("they are not all numbers!\nplease try again.\n")
        continue
    else:
        print("the result is: "+str(result)+"\n")