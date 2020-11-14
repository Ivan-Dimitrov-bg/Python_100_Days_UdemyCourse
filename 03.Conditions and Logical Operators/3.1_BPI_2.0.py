# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Over 25 but below 30 they are slightly overweight
#Over 30 but below 35 they are obese
#Above 35 they are clinically obese.

bmi = float(round(float(weight) / (float(height) * float(height)),0))

if bmi <= 18.5:
  print(f"bpi:{bmi} - underweight")
elif bmi > 18.5 and bmi <= 25:
  print(f"bpi:{bmi} - normal weight")
elif bmi > 25 and bmi <= 30:
  print(f"bpi:{bmi} - slightly overweight")
elif bmi > 30 and bmi <= 35:
   print(f"bpi:{bmi} - obese")
elif bmi > 35:
  print(f"bpi:{bmi} - clinically obese")
