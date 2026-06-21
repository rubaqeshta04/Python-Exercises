# buggy_score_tracker.py — contains 5 bugs

def calculate_average(scores):      # Bug 1
    total = 0
    for score in scores:
        total = total + score
    average = total / len(scores)
    return average

def classify(average):
    if average >= 90:               # Bug 2
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 50 :            # Bug 3
        return "Average"
    else:
        return "Needs Improvement"

student_name = input("Student name: ")
raw_scores   = input("Enter 5 scores separated by commas: ")
scores_list = [float(score) for score in raw_scores.split(",")]
# Bug 4: scores_list contains strings — calculate_average will fail on addition
average = calculate_average(scores_list)
rating  = classify(average)

print(f"\nStudent : {student_name}")
print(f"Average : {round(average, 1)}") # Bug 5: extra closing bracket
print(f"Rating  : {rating}")