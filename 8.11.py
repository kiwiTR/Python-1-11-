def show_magicians(begin_names):
    for name in begin_names:
        print(name)

def make_great(begin_names,end_names):
    while begin_names:
        total =begin_names.pop()
        finish="the Great "+total
        end_names.append(finish)
mag=["tom","andy","mary","duke","lily"]
mag_end=[]
make_great(mag[:],mag_end)
show_magicians(mag_end)
print(mag)