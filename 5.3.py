alien_color="green"
if alien_color=="green":
    print("You get 5 points!")

alien_color="red"
if alien_color=="grenn":
    print("You get 5 points!")

alien_color="grenn"
if alien_color=="green":
    print("You get 5 points!")
else:
    print("You get 10 points!")

alien_color = "grenn"
if alien_color != "green":
    print("You get 10 points!")
else:
    print("You get 5 points!")

alien_color="green"
if alien_color=="grenn":
    print("You get 5 points!")
elif alien_color=="yellow":
    print("You get 10 points!")
else:
    print("You get 15 points!")

age=19
if age<2:
    name="婴儿"
elif age<4:
    name="正蹒跚学步"
elif age<13:
    name="儿童"
elif age<20:
    name="青少年"
elif age<65:
    name="成年人"
else:
    name="老年人"
print("你是一个"+name)

favorite_fruit=["apples","pears","peaches"]
if "apples" in favorite_fruit:
    print("You really like apples!")
if "oranges" in favorite_fruit:
    print("You rally like oranges!")
