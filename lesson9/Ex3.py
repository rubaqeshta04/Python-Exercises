grades = [80, 95, 40, 60, 75]


def analyse_grades(grades):
    passed = 0

    average = sum(grades) / len(grades)
    min_grade = min(grades)
    max_grade = max(grades)

    for grade in grades:
        if grade >= 60:
            passed += 1

    print(average)
    print(min_grade)
    print(max_grade)
    print(passed)


if __name__ == "__main__":
    analyse_grades(grades)