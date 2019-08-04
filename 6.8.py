cat={"type":"cat","owner":"tom"}
dog={"type":"dog","owner":"gaofei"}
fish={"type":"fish","owner":"andy"}
pets=[cat,dog,fish]
for pet in pets:
    print(pet)

favorite_places={"tom":["beijing","shanghai"],"andy":["chongqing"],"lily":["japan","french","america"]}
for name,place in favorite_places.items():
    print(name+"'s favorite places:")
    for goal in place:
        print(place)

nums={"andy":[1,2,3],"tom":[52,6,93],"jan":[3,45,76],"duke":[4,32,5,7],"mary":[1,5]}
for name,num in nums.items():
    print(name+" likes these numbers:")
    for favorite_numbers in num:
        print(favorite_numbers)
    print("\n")

cities={
    "bejing":{
        "country":"China","population":"200w","fact":"prime"
        },
    "shanghai":{
        "country":"China","population":"300w","fact":"economy"
        },
    "chongqing":{"country":"China","population":"500w","fact":"eat"
        },
    }
for city,information in cities.items():
    print(city+"'s basic information:")
    for key1,value1 in information.items():
        print(key1,value1)
    print("\n")