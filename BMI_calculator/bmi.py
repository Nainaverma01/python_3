# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# Formula to claculate BMI is below.
bmi = round(weight / height ** 2)
# 🚨 Don't change the code above 👆
# play around with your upcoming code
if bmi < 18.5 :
    print (f"Your BMI is {bmi},are underweight")
elif bmi < 25 :
    print (f"Your BMI is {bmi},you have a normal weight")
elif bmi < 30 :
    print (f"Your BMI is {bmi},you are slightly overweight")
elif bmi < 35 :
    print (f"Your BMI is {bmi},you are obese")
else :
    print (f"Your BMI is {bmi},you are clinically obesed")
