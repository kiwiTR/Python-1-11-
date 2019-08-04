def city_country(name,country):
    full_name=name+" , "+country
    return full_name
print(city_country("paris","french"))
print(city_country("beijing","china"))
print(city_country("shanghai","china"))

def make_album(name_person,name_soundstrack,songs_numbers=""):
    if songs_numbers:
        total={"name_person":name_person,"name_soundstrack":name_soundstrack,"songs_numbers":songs_numbers}
    else :
        total={"name_person": name_person, "name_soundstrack": name_soundstrack}
    return total
sound1=make_album("tom","GO","5")
print(sound1)
sound2=make_album("andy","sky")
print(sound2)
sound3=make_album("duke","down")
print(sound3)
symbol=True
while symbol:
    print("anytime press 'Q' to quit")
    print("input the messages")
    name1=input("the person:")
    if name1=="Q":
        break
    name2=input("the soundstrack:")
    if name2=="Q":
        break
    judge=input("do you want to add the numbers?(yes/no)")
    if judge=="Q":
        break
    if judge=="yes":
        name3=input("the numbers:")
        if name3=="Q":
            symbol=False
    down=make_album(name1,name2,name3)
    print(down)
    name3=""
    judge2=input("end?(yes/no)")
    if judge2=="yes":
        break

