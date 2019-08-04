class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print(self.cuisine_type)
        print(self.restaurant_name)

    def open_restaurant(self):
        print("the restaurant is now openning.")

    def read_numbers(self):
        print(str(self.number_served)+" have been here.")

    def set_number_served(self,num):
        self.number_served=num

    def increment_number_served(self,num2):
        self.number_served+=num2

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=["pear","apple","orange"]

    def out(self):
        print(self.flavors)

icecreamstand=IceCreamStand("","")
icecreamstand.out()