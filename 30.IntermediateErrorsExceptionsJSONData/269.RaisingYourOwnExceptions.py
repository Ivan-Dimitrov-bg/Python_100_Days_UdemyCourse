# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "Value"}
#     value = a_dictionary["non_existing_key"]
# except FileNotFoundError:
#     file = open("a_file.txt", mode="w")
# except KeyError as error_message:
#     print(f"The Key {error_message} That key did not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that i 've made")
#     file.close()
#     print("File was closed.")

height = float(input("Height(m): "))
weight = int(input("Weight(kg): "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters")

bmi = weight / height**2
print(bmi)
