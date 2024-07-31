class User:

    def __init__(self, user_id, first_name, last_name):         # Constructor
        self.first_name = first_name      # Attributes
        self.last_name = last_name
        self.id = user_id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "John", "Doe")
user_2 = User("002", "Jane", "Doe")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)