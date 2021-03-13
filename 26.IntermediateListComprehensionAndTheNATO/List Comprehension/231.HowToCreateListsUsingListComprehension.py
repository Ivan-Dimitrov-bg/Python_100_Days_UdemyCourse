# number = [1, 2, 3]
# new_list = []
# for n in list:
#     add_1 = n + 1

# new_list.append(add_1)

# example 1
# new_list = [new_item for item in list]
number = [1, 2, 3]
new_list_comprehension = [n+1 for n in number]

# example 2
# new_list = [new_item for item in range()]
range_list = [num*2 for num in range(1, 5)]
print(range_list)

# example 3
# short_names = [new_name for name in names if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)

# example 4
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
upper_case_names = [name.upper() for name in names if len(name) > 4]
print(upper_case_names)