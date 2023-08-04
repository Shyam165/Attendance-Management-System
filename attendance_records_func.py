import datetime
import student_func as stdf

ATTENDANCE_RECORDS_FILE = "attendance_records.txt"

daily_attendance_records = {}
student_database = stdf.view_students()
# Function to save the daily attendance records to the file
def save_attendance_records():
    with open(ATTENDANCE_RECORDS_FILE, "w") as file:
        for date, records in daily_attendance_records.items():
            for record in records:
                file.write(f"{date},{record['student_id']},{record['name']},{record['status']}\n")


# Function to load the daily attendance records from the file
def load_attendance_records():
    try:
        with open(ATTENDANCE_RECORDS_FILE, "r") as file:
            for line in file:
                date, student_id, name, status = line.strip().split(",")
                if date not in daily_attendance_records:
                    daily_attendance_records[date] = []
                daily_attendance_records[date].append({"student_id": student_id, "name": name, "status": status})
    except FileNotFoundError:
        # The file doesn't exist yet, create it when the first attendance is marked.
        pass


# Function to mark attendance of students
def mark_attendance(date, student_ids_present):
    records = []
    for student_id in student_ids_present:
        name = student_database.get(student_id, "Unknown")
        record = {"student_id": student_id, "name": name, "status": "Present"}
        records.append(record)

    if date in daily_attendance_records:
        daily_attendance_records[date].extend(records)
    else:
        daily_attendance_records[date] = records

    save_attendance_records()
    return "Attendance marked successfully."


def view_attendance_records():
    for date, records in daily_attendance_records.items():
        print(f"Date: {date}")
        for record in records:
            print(f"Student ID: {record['student_id']}, Name: {record['name']}, Status: {record['status']}")


def generate_daily_report(date):
    if date in daily_attendance_records:
        report_file = f"daily_attendance_report_{date}.txt"
        with open(report_file, "w") as file:
            file.write(f"Date: {date}\n")
            for record in daily_attendance_records[date]:
                file.write(f"Student ID: {record['student_id']}, Name: {record['name']}, Status: {record['status']}\n")
        print(f"Daily attendance report for {date} generated successfully.")
    else:
        print(f"No attendance records found for {date}.")


def generate_weekly_report(start_date):
    try:
        year, month, day = map(int, start_date.split("-"))
        start_date_obj = datetime.date(year, month, day)
        end_date_obj = start_date_obj + datetime.timedelta(days=6)
        end_date = end_date_obj.strftime("%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD format.")
        return

    report_file = f"weekly_attendance_report_{start_date}.txt"

    with open(report_file, "w") as file:
        file.write(f"Weekly Attendance Report ({start_date} to {end_date})\n")
        for i in range(7):
            current_date_obj = start_date_obj + datetime.timedelta(days=i)
            current_date = current_date_obj.strftime("%Y-%m-%d")
            if current_date in daily_attendance_records:
                file.write(f"\nDate: {current_date}\n")
                for record in daily_attendance_records[current_date]:
                    file.write(f"Student ID: {record['student_id']}, Name: {record['name']}, Status: {record['status']}\n")

    print(f"Weekly attendance report from {start_date} to {end_date} generated successfully.")


def generate_monthly_report():
    report_file = "monthly_attendance_report.txt"

    with open(report_file, "w") as file:
        for date, records in daily_attendance_records.items():
            file.write(f"Date: {date}\n")
            for record in records:
                file.write(f"Student ID: {record['student_id']}, Name: {record['name']}, Status: {record['status']}\n")

    print("Monthly attendance report generated successfully.")
