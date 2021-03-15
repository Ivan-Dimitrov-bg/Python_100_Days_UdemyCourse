# file not found
#
# with open("a_file.txt", mode="r") as fileName:
#     fileName.read()
# ------------------------------------------------

#keyError

# a_dictionary = {"key": "Value"}
# value = a_dictionary["non_existing_key"]

# ---------

# IndexError  - IndexError: list index out of range
# fruit_list = ["Apple", "Banna"]
# fruit = fruit_list[2]

# TypeError: can only concatenate str (not "int") to str
# text = "abc"
# print(text + 5)

# python_theory
# try  - Something that might cause an Exception
# except - Do this if there was an exception
# else - Do this if there were no exception
# finally - Do this no matter what happens
# raise - raise your own errors

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "Value"}
    value = a_dictionary["non_existing_key"]
except FileNotFoundError:
    file = open("a_file.txt", mode="w")
except KeyError as error_message:
    print(f"The Key {error_message} That key did not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
