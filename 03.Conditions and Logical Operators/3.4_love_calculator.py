# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

#"Your score is 47, you are alright together."
#"Your score is 125, you go together like coke and mentos."
#"Your score is 54."

name1 = name1.lower()
name2 = name2.lower()

count_letter = name1.count('t')
count_letter += name1.count('r')
count_letter += name1.count('u')
count_letter += name1.count('e')

count_letter += name2.count('t')
count_letter += name2.count('r')
count_letter += name2.count('u')
count_letter += name2.count('e')

count_letters_in_TRUE = count_letter
#print(count_letters_in_TRUE)

count_letter = name1.count('l')
count_letter += name1.count('o')
count_letter += name1.count('v')
count_letter += name1.count('e')

count_letter += name2.count('l')
count_letter += name2.count('o')
count_letter += name2.count('v')
count_letter += name2.count('e')

count_letters_in_Love = count_letter
#print(count_letters_in_Love)

#print(f"{count_letters_in_TRUE}{count_letters_in_Love}")

score = int(f"{count_letters_in_TRUE}{count_letters_in_Love}")
if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")