students = [
    {"name": "Ali", "score": 80},
    {"name": "Sara", "score": 50},
    {"name": "Omar", "score": 70},
]

passed_students = []

for student in students:
    if student["score"] >= 60:
        passed_students.append(student)

print(passed_students)
