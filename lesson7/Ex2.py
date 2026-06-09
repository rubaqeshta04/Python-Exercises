# Exercise 2 — BMI Calculator

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / height ** 2
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi <= 24.9:
    print("Category: Normal")
elif bmi <= 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")
