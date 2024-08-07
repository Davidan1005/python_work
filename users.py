class User:
    """Models users"""

    def __init__(self, first_name, last_name, age, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.login_attempts = 0

    def describe_user(self):
        """describes users"""
        print("your name is " + self.first_name.title() + " "
              + self.last_name.title() + " and you are " + str(self.age)
              + " years old")

    def greet_user(self):
        """greets users"""
        print("Hello "+self.first_name.title()+"!")

    def increment_login_attempts(self):
        """Increments login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    """Privileges of each admin"""

    def __init__(self, *privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    """Models the admin of a website"""

    def __init__(self, first_name, last_name, age, phone_number, *privileges):
        super().__init__(first_name, last_name, age, phone_number)
        self.privileges = Privileges(privileges)

# admin_privileges = Privileges("can ban users","can change settings")


user1 = User("Cyrus", "Nduka", 19, 2345)
admin1 = Admin("Cyrus", "Nduka", 19, 2345,
               "can ban users", "can change settings")
admin1.privileges.show_privileges()
user1.describe_user()
user1.greet_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)
