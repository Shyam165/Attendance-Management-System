# Attendance Management System with User Authentication

This repository contains a Python implementation of an Attendance Management System with User Authentication. The system allows administrators to manage student information, mark daily attendance, and generate monthly attendance reports. The system also provides user authentication to ensure that only authorized users can access administrative functions.

## Key Features

1.User Authentication: The system supports user registration and login functionality. Administrators can register new users (with admin privileges) by providing a username and password. Users can log in using their credentials to access administrative functions.

2.Student Information Management: The system allows administrators to add new students, view the list of existing students, update student information, and delete students from the database.

3.Daily Attendance Management: Administrators can mark the attendance of students on a daily basis. The system saves daily attendance records to a file.

4.Monthly Attendance Report: The system generates monthly attendance reports, consolidating the daily attendance data for each student. The monthly reports are saved to a separate file.

# File Structure

1.main.py: This is the main Python script that contains the implementation of the Attendance Management System. It includes functions for user authentication, student management, attendance marking, and generating monthly reports.

2.user_credentials.txt: This file stores user credentials (username and password) in a comma-separated format. The file is used for user authentication.

3.attendance_records.txt: This file stores daily attendance records in a comma-separated format. The file is used to save and load daily attendance data.

4.monthly_attendance_report.txt: This file stores monthly attendance reports. It is generated and updated when monthly reports are generated.

# How to Use

1.Clone the repository to your local machine.
2.Run the main.py script using Python.
3.The system will display a menu for login or exit options.
4.If you are an admin, you can register new users, manage student information, mark attendance, and generate monthly reports.
5.If you are a regular user, you can only add students, view the list of students, and log out.

# Dependencies

The script does not require any external dependencies. It uses Python's built-in libraries to handle file operations and user input.

# Contributing

Contributions to the project are welcome. If you find any issues or want to add new features, please submit a pull request.

# License

This project is licensed under the MIT License.

# Note

This project was created for educational purposes and might not be suitable for production use without additional security measures. Please use it responsibly and adapt it to your specific needs as required.
