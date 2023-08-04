import attendance_function as atf
import student_inf as stdf
import user_credentials_func as utf

def main():
    utf.load_user_credentials()
    atf.load_attendance_records()
    stdf.load_student_data()
    print("Welcome to the Attendance Management System")
    while True:
        print("\nOptions:")
        print("1. Login\n2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            message = utf.login_user(username, password)
            print(message)

            if message == "Login successful.":
                if username == "shyam1":  # Check if the user is the admin
                    while True:
                        print("\nOptions:")
                        print("1. Register User\n2. Add Student\n3. View Students\n4. Update Student\n5. Delete Student\n6. Mark Attendance\n7. Generate Monthly Report\n8. Logout")
                        user_choice = input("Enter your choice: ")

                        if user_choice == "1":
                            new_username = input("Enter a username: ")
                            new_password = input("Enter a password: ")
                            message = utf.register_user(new_username, new_password)
                            print(message)

                        elif user_choice == "2":
                            student_id = input("Enter the Student ID: ")
                            name = input("Enter the Student's Name: ")
                            message = stdf.add_student(student_id, name)
                            print(message)

                        elif user_choice == "3":
                            students = stdf.view_students()
                            print("Students in the database:")
                            for student_id, name in students.items():
                                print(f"Student ID: {student_id}, Name: {name}")

                        elif user_choice == "4":
                            student_id = input("Enter the Student ID to update: ")
                            new_name = input("Enter the new Name: ")
                            message = stdf.update_student(student_id, new_name)
                            print(message)

                        elif user_choice == "5":
                            student_id = input("Enter the Student ID to delete: ")
                            message = stdf.delete_student(student_id)
                            print(message)

                        elif user_choice == "6":
                            date = input("Enter the date (YYYY-MM-DD): ")
                            student_ids_present = input("Enter Student IDs present: ").split(",")
                            attendance_record = atf.mark_attendance(date, student_ids_present)
                            print("Attendance marked for:")
                            for student_id, name in attendance_record.items():
                                print(f"Student ID: {student_id}, Name: {name}")

                        elif user_choice == "7":
                            atf.generate_monthly_report()
                            atf.save_monthly_report()
                            print("Monthly report generated successfully.")

                        elif user_choice == "8":
                            print("Logged out successfully.")
                            break

                        else:
                            print("Invalid choice. Please try again.")

                else:
                    while True:
                        print("\nOptions:")
                        print("1. Add Student\n2. View Students\n3. Logout")
                        user_choice = input("Enter your choice: ")

                        if user_choice == "1":
                            student_id = input("Enter the Student ID: ")
                            name = input("Enter the Student's Name: ")
                            message = stdf.add_student(student_id, name)
                            print(message)
                        elif user_choice == "2":
                            students = stdf.view_students()
                            print("Students in the database:")
                            for student_id, name in students.items():
                                print(f"Student ID: {student_id}, Name: {name}")

                        elif user_choice == "3":
                            print("Logged out successfully.")
                            break

                        else:
                            print("Invalid choice. Please try again.")

        elif choice == "2":
            print("Exiting the Attendance Management System.")
            utf.save_user_credentials()
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
