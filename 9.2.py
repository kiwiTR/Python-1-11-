class User():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

    def describe_user(self):
        print("these are the messages:")
        print(self.first_name,self.last_name)

    def greet_user(self):
        print("hello!!! " + self.first_name + " "+self.last_name)

tom=User("t","om")
tom.describe_user()
tom.greet_user()

user2=User("ada","wang")
user2.describe_user()
user2.greet_user()

user3=User("ziming","Li")
user3.describe_user()
user2.greet_user()