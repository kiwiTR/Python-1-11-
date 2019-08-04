rivers={"Changjiang":"China","nile":"Egypt","missisipy":"America"}
for river,country in rivers.items():
    print("The "+river+" runs through "+country+".")
print("\n")
favorite_languages={"jen":"python","sarah":"c","edward":"ruby","phil":"python",}
names=["jen","tom","andy","phil"]
for name in favorite_languages:
    if name in names:
        print("Thanks for "+name+" .")
    else:
        print("I will invate "+name+" to join us.")