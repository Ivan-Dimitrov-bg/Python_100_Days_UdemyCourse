# read
file = open("my_file.txt")
contents = file.read()
print(contents)

file.close()

# no need to close the file
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# write

"overwrite"  "it will create new file if file doesn't exist"
with open("my_file.txt", mode="w") as file:
    file.write("New Text")

# append
with open("my_file.txt", mode="a") as file:
    file.write("New Text")