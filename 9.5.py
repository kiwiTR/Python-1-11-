class User():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0

    def describe_user(self):
        print("these are the messages:")
        print(self.first_name,self.last_name)

    def greet_user(self):
        print("hello!!! " + self.first_name + " "+self.last_name)

    def increment_attempts(self):
        self.login_attempts+=1

    def reset_login_attempts(self):
        self.login_attempts=0

user=User("ada","wang")
print(str(user.login_attempts))
for i in range(10):
    user.increment_attempts()
print(str(user.login_attempts))
user.reset_login_attempts()
print(str(user.login_attempts))