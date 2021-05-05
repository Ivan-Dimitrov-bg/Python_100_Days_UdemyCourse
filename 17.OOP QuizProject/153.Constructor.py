class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        print("new user being created...")


user_1 = User("001", "angela")
# user_1.id = "001"
# user_1.username = "angela"
print(user_1.id)
print(user_1.username)

user_2 = User("002", "Jack")
# user_2.id = "002"
# user_2.name = "Jack"
# ------------------
