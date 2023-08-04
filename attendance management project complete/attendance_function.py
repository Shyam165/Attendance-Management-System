import student_inf as stdf

USER_DATABASE_FILE = "user_credentials.txt"
ATTENDANCE_RECORDS_FILE = "attendance_records.txt"
MONTHLY_REPORT_FILE = "monthly_attendance_report.txt"

user_database = {"shyam1":"shyam2"}
student_database = stdf.view_students()
daily_attendance_records = {}
weekly_attendance_records = {}
monthly_attendance_records = {}

def save_attendance_records():
    with open(ATTENDANCE_RECORDS_FILE, "w") as file:
        for date, records in daily_attendance_records.items():
            for student_id, name in records.items():
                # Add the attendance status (e.g., "Present") along with the date, student_id, and name
                file.write(f"{date},{student_id},{name},Present\n")

def load_attendance_records():
    try:
        with open(ATTENDANCE_RECORDS_FILE, "r") as file:
            for line in file:
                date, student_id, name, attendance_status = line.strip().split(",")
                if date not in daily_attendance_records:
                    daily_attendance_records[date] = {}
                daily_attendance_records[date][student_id] = {"name": name, "status": attendance_status}
    except FileNotFoundError:
        # The file doesn't exist yet, create it when the first attendance is marked.
        pass


# Marking Attendance
def mark_attendance(date, student_ids_present):
    attendance_record = {}
    for student_id in student_ids_present:
        if student_id in student_database:
            attendance_record[student_id] = student_database[student_id]
    daily_attendance_records[date] = attendance_record
    save_attendance_records()  # Save the attendance records immediately after marking attendance
    return attendance_record

# generating and saving the monthly reports in text file

def generate_monthly_report():
    for date, records in daily_attendance_records.items():
        year, month, day = map(int, date.split("-"))
        key = f"{year}-{month}"
        if key not in monthly_attendance_records:
            monthly_attendance_records[key] = {}
        for student_id, data in records.items():
            name = data["name"]
            attendance_status = data["status"]
            monthly_attendance_records[key][student_id] = {"name": name, "status": attendance_status}


def save_monthly_report():
    with open(MONTHLY_REPORT_FILE, "w") as file:
        for key, records in monthly_attendance_records.items():
            file.write(f"Month: {key}\n")
            for student_id, data in records.items():
                name = data["name"]
                attendance_status = data["status"]
                file.write(f"{student_id},{name},{attendance_status}\n")

