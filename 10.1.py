with open("learning_python.txt") as file_object:
    txt1=file_object.read()
    print(txt1)

with open("learning_python.txt") as file_object:
    for txt2 in file_object:
        print(txt2.rstrip())

with open("learning_python.txt") as file_object:
    txt3=file_object.readlines()
print(txt3)