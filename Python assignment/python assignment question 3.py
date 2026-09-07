# 3.(I)Dictionary of students and marks
students = {
    "Alice": 85,
    "Benjamin": 92,
    "Tinotenda": 78,
    "Tinashe": 88,
    "Bervaly":  90
}

# This code Display all students and their marks
print("Students and their marks:")
for name, mark in students.items():
    print(f"{name}: {mark}")

# this line of code below is for finding the student with the highest mark
top_student = max(students, key=students.get)
print(f"\nStudent with the highest mark: {top_student} ({students[top_student]})")


