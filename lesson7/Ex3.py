# Exercise 3 — Electricity Bill

kwh = float(input("Enter kWh consumed: "))

if kwh <= 100:
    total = kwh * 0.40
elif kwh <= 300:
    total = (100 * 0.40) + ((kwh - 100) * 0.65)
else:
    total = (100 * 0.40) + (200 * 0.65) + ((kwh - 300) * 0.95)

print(f"Total bill: R${total:.2f}")
