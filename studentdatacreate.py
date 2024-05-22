import csv

# Define the student data
student_data = [
    {"StudentID": 1001, "Name": "John Doe", "Semester": "Spring 2023", "Course": "Mathematics", "Grade": "A"},
    {"StudentID": 1001, "Name": "John Doe", "Semester": "Spring 2023", "Course": "Physics", "Grade": "B+"},
    {"StudentID": 1001, "Name": "John Doe", "Semester": "Spring 2023", "Course": "Chemistry", "Grade": "A-"},
    {"StudentID": 1001, "Name": "John Doe", "Semester": "Fall 2023", "Course": "Mathematics", "Grade": "A-"},
    {"StudentID": 1001, "Name": "John Doe", "Semester": "Fall 2023", "Course": "Computer Science", "Grade": "B"},
    {"StudentID": 1001, "Name": "John Doe", "Semester": "Fall 2023", "Course": "Biology", "Grade": "A"},
    {"StudentID": 1002, "Name": "Jane Smith", "Semester": "Spring 2023", "Course": "Mathematics", "Grade": "B+"},
    {"StudentID": 1002, "Name": "Jane Smith", "Semester": "Spring 2023", "Course": "Physics", "Grade": "A"},
    {"StudentID": 1002, "Name": "Jane Smith", "Semester": "Spring 2023", "Course": "English", "Grade": "A-"},
    {"StudentID": 1002, "Name": "Jane Smith", "Semester": "Fall 2023", "Course": "Mathematics", "Grade": "A"},
    {"StudentID": 1002, "Name": "Jane Smith", "Semester": "Fall 2023", "Course": "Computer Science", "Grade": "A-"},
    {"StudentID": 1002, "Name": "Jane Smith", "Semester": "Fall 2023", "Course": "Biology", "Grade": "B+"}
]

# Define the CSV file name
csv_file = 'student_details.csv'

# Write the data to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["StudentID", "Name", "Semester", "Course", "Grade"])
    writer.writeheader()
    for data in student_data:
        writer.writerow(data)

print(f"{csv_file} has been created successfully.")
