
#example input = 156 178 165 171 187
#example output = 171

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum_height = 0
countItmes = 0
for student_height in student_heights:
    sum_height += student_height
    countItmes += 1

average = sum_height / countItmes

print(average)