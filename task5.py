students = {
    "Rahim": 85,
    "Karim": 90,
    "Suma": 78,
    "Joya": 92
}

# 1. Print all student names

print("Student Names:")
for name in students:
    print(name)



# 2. Show students with marks > 80

print("\nStudents with marks > 80:")
for name, marks in students.items():
    if marks > 80:
        print(name, marks)



# 3. Find top scorer

top_student = max(students, key=students.get)
print("\nTop Scorer:")
print(top_student, students[top_student])