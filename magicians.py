def show_magicians(names):
    for name in names:
        print(name)

def make_great(names):
    change_names = []
    for name in names:
        total = "the Great " + name
        change_names.append(total)
    return change_names


