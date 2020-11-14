# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#There are 365 days in a year, 52 weeks in a year and 12 months in a year.

daysEnd = 90 * 365
weeksEnd = 90 * 52
monthEnd = 90

daysNow = int(age) * 365
weeksNow = int(age) * 52
monthNow = int(age)

print("You have {} days, {} weeks, and {} months left.".format(daysEnd - daysNow, weeksEnd - weeksNow, monthEnd - monthNow))