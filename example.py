weight= float(input("Your Weight in kg's:"))
height= float(input("Your Height in meters:"))

bmi=round(weight/(height)**2)
if bmi<=16.0:
    print(f" your BMI is {bmi}, your Under Weight")
elif bmi<=24.9:
    print(f"your BMI is {bmi}, your Weight in Normal range")
elif bmi<=29.9:
    print(f"your BMI is {bmi}, your Over weighted pree-obese")
elif bmi<=34.9:
    print(f"your BMI is {bmi}, your obese stage 1")
else:
    print(f" your BMI is {bmi}, your obese state 2")
print("take care bye bye")
