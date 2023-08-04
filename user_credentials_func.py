USER_DATABASE_FILE = "user_credentials.txt"
user_database = {"shyam1": "shyam2"}


# Function to read the user credentials from the file into the user_database dictionary
def load_user_credentials():
    try:
        with open(USER_DATABASE_FILE, "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                user_database[username] = password
    except FileNotFoundError:
        # The file doesn't exist yet, create it when the first admin registers.
        pass


# Function to save the user credentials from the user_database dictionary to the file
def save_user_credentials():
    with open(USER_DATABASE_FILE, "w") as file:
        for username, password in user_database.items():
            file.write(f"{username},{password}\n")


# User Authentication
def register_user(username, password):
    if username in user_database:
        return "Username already exists."
    user_database[username] = password
    save_user_credentials()
    return "Registration successful."


def login_user(username, password):
    if username not in user_database or user_database[username] != password:
        return "Invalid username or password. You are not an authenticated person."
    return "Login successful."
