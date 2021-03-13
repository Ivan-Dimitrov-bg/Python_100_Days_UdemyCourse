# Write your code above 👆

with open("file1.txt", mode='r') as file1:
    file1 = file1.readlines()
# print (file1)
with open("file2.txt", mode='r') as file2:
    file2 = file2.readlines()
# print(file2)
result = [int(number.strip()) for number in file1 if number in file2]
print(result)