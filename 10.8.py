txt=["cats.txt","dogs.txt","fishes.txt"]
for file_name in txt:
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("the "+file_name+" file is not found.")
    else:
        print(contents+"\n")