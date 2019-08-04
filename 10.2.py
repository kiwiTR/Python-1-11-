with open("learning_python.txt") as file_object:
    for txt1 in file_object:
        txt2=txt1.replace("python","c")
        print(txt2.rstrip())