import openpyxl
students_data = [
    ["John", 20, "Computer Science", "Software Engineering", [85, 90, 80, 95, 88]],
    ["Emily", 21, "Mathematics", "Pure Mathematics", [75, 82, 80, 88, 90]],
    ["Michael", 19, "Biology", "Genetics", [90, 92, 88, 85, 86]],
    ["Sophia", 22, "Chemistry", "Organic Chemistry", [78, 85, 92, 76, 80]],
    ["Daniel", 20, "Physics", "Quantum Mechanics", [92, 88, 85, 90, 94]]
]
workbook = openpyxl.Workbook()
sheet = workbook.active
headers = ["Name", "Age", "Faculty", "Specialty", "Grades", "Average Grade"]
sheet.append(headers)
for student in students_data:
    name = student[0]
    age = student[1]
    faculty = student[2]
    specialty = student[3]
    grades = student[4]
    average_grade = sum(grades) / len(grades)
    sheet.append([name, age, faculty, specialty, grades, average_grade])

workbook.save("students_with_semester_grades.xlsx")