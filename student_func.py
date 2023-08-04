STUDENT_DATA_FILE = "student_data.txt"
student_database = {}

# Function to save the student data to the file
def save_student_data():
    with open(STUDENT_DATA_FILE, "w") as file:
        for student_id, name in student_database.items():
            file.write(f"{student_id},{name}\n")


# Function to load the student data from the file
def load_student_data():
    try:
        with open(STUDENT_DATA_FILE, "r") as file:
            for line in file:
                student_id, name = line.strip().split(",")
                student_database[student_id] = name
    except FileNotFoundError:
        # The file doesn't exist yet, create it when the first student is added.
        pass


def add_student(student_id, name):
    if student_id in student_database:
        return "Student ID already exists."
    student_database[student_id] = name
    save_student_data()
    return "Student added successfully."


def view_students():
    return student_database


def update_student(student_id, new_name):
    if student_id not in student_database:
        return "Student ID not found."
    student_database[student_id] = new_name
    save_student_data()
    return "Student information updated successfully."


def delete_student(student_id):
    if student_id not in student_database:
        return "Student ID not found."
    del student_database[student_id]
    save_student_data()
    return "Student deleted successfully."
