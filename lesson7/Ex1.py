# Exercise 1 — Season Detector

month = int(input("Enter a month number (1–12): "))

if month in [12, 1, 2]:
    print("Summer")
elif month in [3, 4, 5]:
    print("Autumn")
elif month in [6, 7, 8]:
    print("Winter")
elif month in [9, 10, 11]:
    print("Spring")
else:
    print("Invalid")
