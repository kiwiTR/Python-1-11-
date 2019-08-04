class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(self.cuisine_type)
        print(self.restaurant_name)

    def open_restaurant(self):
        print("the restaurant is now openning.")

restaurant=Restaurant("SKY","china")
print(restaurant.restaurant_name,restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2=Restaurant("GO","french")
restaurant2.describe_restaurant()

restaurant3=Restaurant("OUT","america")
restaurant3.describe_restaurant()
