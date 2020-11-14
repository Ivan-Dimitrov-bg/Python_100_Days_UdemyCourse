#Write your code below this row 👇

for n in range(1, 101):
  if n % 15 == 0:
     print("FizzBizz")
  elif n % 3 == 0:
    print("Fizz")
  elif n % 5 == 0:
    print("Bizz")
  else:
    print(n)