class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1
user_1 = User("001", "Kevin")
user_2 = User("002", "Maria")

print(f"Followers of {user_1.name}: {user_1.followers}")
print(f"Followers of {user_2.name}: {user_2.followers}")

print(f"{user_1.name} followed {user_2.name}")
user_1.follow(user_2)

print(f"Followers of {user_2.name}: {user_2.followers}")