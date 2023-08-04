# Make A Stranger Chat Bot With Given Instructions : 
# 1. First Need To Log In or Sign UP.
# 2. Declare The Stranger Names.
# 3. Gives Only 10 Lines To Chat.
# 4. Prompt: Continue Or Stop
# 5. Continue: Gives 10 Lines Or More.
# 6. Exit: Stop Program.


import random

# Pre-defined list of stranger names
stranger_names = ["John", "Alice", "Michael", "Sophia", "William"]

# Dictionary to store user credentials (username: password)
user_database = {}

def signup():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    if username in user_database:
        print("Username already exists. Please try again.")
    else:
        user_database[username] = password
        print("Sign up successful. Please log in.")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username not in user_database or user_database[username] != password:
        print("Invalid username or password. Please try again.")
        return False
    else:
        print("Login successful.")
        return True

def chat_with_stranger(stranger_name):
    print(f"Connected with {stranger_name}. You can chat for 10 lines:")
    for i in range(10):
        user_input = input("You: ")
        print(f"{stranger_name}: Hi, {user_input}.")
    print("Chat limit reached. Do you want to continue chatting? (yes/no)")
    continue_chatting = input().lower()
    return continue_chatting == "yes"

def main():
    print("Welcome to the Stranger Chat Bot!")

    while True:
        user_choice = input("1. Log In\n2. Sign Up\n3. Exit\nEnter your choice: ")

        if user_choice == "1":
            if login():
                break
        elif user_choice == "2":
            signup()
        elif user_choice == "3":
            print("Exiting the Stranger Chat Bot.")
            break
        else:
            print("Invalid choice. Please try again.")

    while True:
        stranger_name = random.choice(stranger_names)
        continue_chatting = chat_with_stranger(stranger_name)

        if not continue_chatting:
            print("Thank you for chatting with the Stranger Chat Bot!")
            break

if __name__ == "__main__":
    main()
