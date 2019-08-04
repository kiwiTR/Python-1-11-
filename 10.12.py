import json
file_name="numbers.jaon"
try:
    with open(file_name) as f_obj:
        number=json.load(f_obj)
except FileNotFoundError:
    with open(file_name,"a") as f_obj:
        num1=input("tell me a nuember which you loved.")
        json.dump(num1,f_obj)
else:
    print("I know your favorite number! It's "+number+".")