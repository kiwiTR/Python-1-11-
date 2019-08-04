print("please input two numbers and I will add them.")
num1=input("the first:")
num2=input("the second:")
try:
    result=int(num1)+int(num2)
except ValueError:
    print("they are not all numbers!")
else:
    print("the result is: "+str(result))