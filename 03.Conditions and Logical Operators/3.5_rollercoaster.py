print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    print("Child tickets are $5.")
  elif age <= 18:
    print("Youth tickets are $7.")
  else:
    print("Adult tickets are $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")
