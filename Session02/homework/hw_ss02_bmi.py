height_cm = float(input("Your height in cm?"))
mass = float(input("Your weight in kg?"))
height_m = height_cm / 100
BMI = mass / height_m ** 2
print(BMI)
if BMI < 16:
    print("severely underweight")
elif 16 <= BMI < 18.5:
    print("underweight")
elif 18.5 <= BMI < 25:
    print("normal")
elif 25 <= BMI <= 30:
    print("overweight")
else:
    print("obese")
