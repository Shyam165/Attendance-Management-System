# Attendance Management System
The Attendance Management System is a command-line Python application that allows administrators to manage student data, mark student attendance, and generate daily, weekly, and monthly attendance reports. The system utilizes file handling to store user credentials, student data, and attendance records in text files.

## Features
1.User Authentication:
•	Administrators can register and login using a username and password.
•	Passwords are securely stored in the user credentials file.
2. Student Information Management:
•	Administrators can add, view, update, and delete student information.
•	Student data is stored in the student data file.
3.Attendance Management:
•	Administrators and students can mark attendance for a specific date.
•	Attendance records are stored in the attendance records file.
4.Attendance Reports:
•	Administrators can generate daily, weekly, and monthly attendance reports.

## Prerequisites
•	Python 3.x installed on your system.
## Getting Started
1. Clone the repository to your local machine:
•	git clone https://github.com/your_username/attendance-management-system.git
•	cd attendance-management-system
1.Install the required packages:
•	pip install -r requirements.txt
## Usage
1.Run the application:
•	python attendance_system.py
1.On the main menu, you have two options:
•	Login: To access administrative features.
•	Exit: To exit the application.
2.If you choose to login, you need to provide valid admin credentials (username and password) to access administrative features.
3.Admin Features:
•	Register User: Add new admin users to the system.
•	Add Student: Add student information to the system.
•	View Students: View a list of all students in the database.
•	Update Student: Update student information.
•	Delete Student: Remove a student from the database.
•	Mark Attendance: Mark attendance for students on a specific date.
•	View Attendance Records: View attendance records for all dates.
•	Generate Daily Report: Generate a report for a specific date.
•	Generate Weekly Report: Generate a report for a specific week.
•	Generate Monthly Report: Generate a report for the entire month.
## Data Files
•	user_credentials.txt: Stores admin user credentials.
•	student_data.txt: Stores student information.
•	attendance_records.txt: Stores attendance records.
## Important Notes
•	Student names in attendance records and reports are displayed based on their IDs in the student database.
•	If a student ID is not found in the database, "Unknown" will be displayed as the student name in attendance records and reports.
## Contributing
Contributions to this project are welcome! Feel free to create pull requests and raise issues for any improvements or bug fixes.
## License
This project is licensed under the MIT License - see the LICENSE file for details.
## Acknowledgments
This project was developed as a practice exercise and is not intended for production use. It demonstrates the use of Python file handling, basic data management, and user authentication.
