student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62
}

student_grades = {}

for k,v in student_scores.items():
    if v >= 91:
        grade = "Outstanding"
    elif v >= 81:
        grade = "Exceeds Expectations"
    elif v >= 71:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[k] = grade

print(student_grades)