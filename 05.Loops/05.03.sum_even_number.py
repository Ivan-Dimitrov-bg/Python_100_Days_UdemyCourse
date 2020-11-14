#Write your code below this row 👇
sum = 0
for n in range(0, 101, 2):
  sum += n

print(sum)

#second solution
sum = 0
for n in range(0, 101):
  if n % 2 == 0:
    sum += n

print(sum)

