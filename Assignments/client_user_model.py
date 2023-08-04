class User:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}, Age: {self.age}"
class Client:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def display_users(self):
        for user in self.users:
            print(user)

def main():
    client = Client()

    user1 = User("john_doe", "john@example.com", 30)
    user2 = User("alice_smith", "alice@example.com", 25)

    client.add_user(user1)
    client.add_user(user2)

    print("List of Users:")
    client.display_users()

if __name__ == "__main__":
    main()
