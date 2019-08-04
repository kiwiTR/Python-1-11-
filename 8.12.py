def show_sandwich(*foods):
    print("You have ordered:")
    print(*foods)
show_sandwich("fish")
show_sandwich("meat","fruit")
show_sandwich("beef","milk","mushroom")

def build_profile(first,last,**user_info):
    profile={}
    profile["first_name"]=first
    profile["last_name"]=last
    for key,value in user_info.items():
        profile[key]=value
    return profile
message1=build_profile("weiqi","wang",location="china",field="computer")
print(message1)

def build_car(company,type,**car_info):
    message={}
    message["company"]=company
    message["type"]=type
    for key,value in car_info.items():
        message[key]=value
    return message
car_information=build_car("dazhong","T-130",color="blue",tow_package=True)
print(car_information)