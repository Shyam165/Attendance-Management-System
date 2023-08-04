import user_credentials_func as ucf
import student_func as stdf
import attendance_records_func as atdf


def main():
    ucf.load_user_credentials()
    stdf.load_student_data()
    atdf.load_attendance_records()

    print("Welcome to the Attendance Management System")
    while True:
        print("\nOptions:")
        print("1. Login\n2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            message = ucf.login_user(username, password)
            print(message)

            if message == "Login successful.":
                if username == "shyam1":  # Check if the user is the admin
                    while True:
                        print("\nOptions:")
                        print("1. Register User\n2. Add Student\n3. View Students\n4. Update Student")
                        print("5. Delete Student\n6. Mark Attendance\n7. View Attendance Records")
                        print("8. Generate Daily Report\n9. Generate Weekly Report\n10. Generate Monthly Report")
                        print("11. Logout")
                        user_choice = input("Enter your choice: ")

                        if user_choice == "1":
                            new_username = input("Enter a username: ")
                            new_password = input("Enter a password: ")
                            message = ucf.register_user(new_username, new_password)
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
                            student_ids_present = input("Enter Student IDs present (comma-separated): ").split(",")
                            message = atdf.mark_attendance(date, student_ids_present)
                            print(message)

                        elif user_choice == "7":
                            print("Attendance Records:")
                            atdf.view_attendance_records()

                        elif user_choice == "8":
                            date = input("Enter the date (YYYY-MM-DD) for the daily report: ")
                            atdf.generate_daily_report(date)

                        elif user_choice == "9":
                            start_date = input("Enter the start date (YYYY-MM-DD) for the weekly report: ")
                            atdf.generate_weekly_report(start_date)

                        elif user_choice == "10":
                            atdf.generate_monthly_report()

                        elif user_choice == "11":
                            print("Logged out successfully.")
                            break

                        else:
                            print("Invalid choice. Please try again.")

                else:
                    while True:
                        print("\nOptions:")
                        print("1. Mark Attendance\n2. View Attendance Records\n3. Logout")
                        user_choice = input("Enter your choice: ")

                        if user_choice == "1":
                            date = input("Enter the date (YYYY-MM-DD): ")
                            student_ids_present = input("Enter Student IDs present (comma-separated): ").split(",")
                            message = atdf.mark_attendance(date, student_ids_present)
                            print(message)

                        elif user_choice == "2":
                            print("Attendance Records:")
                            atdf.view_attendance_records()

                        elif user_choice == "3":
                            print("Logged out successfully.")
                            break

                        else:
                            print("Invalid choice. Please try again.")

        elif choice == "2":
            print("Exiting the Attendance Management System.")
            ucf.save_user_credentials()
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
