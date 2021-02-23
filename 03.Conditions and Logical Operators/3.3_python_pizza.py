print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

prise = 0
if size == "S":
  prise = 15
if size == "M":
  prise = 20
if size == "L":
  prise = 25

if add_pepperoni == "Y":
  if size == "S":
    prise += 2
  else:
    prise += 3

if extra_cheese == "Y":
  prise += 1

print(f"Your final bill is: ${prise}.")



# #Write your code above this line 👆
# # 🚨 Do NOT modify the code below this line 👇
#
#
# with open('testing_copy.py', 'w') as file:
#   file.write('def test_func():\n')
#   with open('153Constructor.py', 'r') as original:
#     f2 = original.readlines()[0:40]
#     for x in f2:
#       file.write("    " + x)
#
#
# import testing_copy
# import unittest
# from unittest.mock import patch
# from io import StringIO
# import os
#
# class MyTest(unittest.TestCase):
#   def run_test(self, given_answer, expected_print):
#     with patch('builtins.input', side_effect=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:
#       testing_copy.test_func()
#       self.assertEqual(fake_out.getvalue(), expected_print)
#
#   def test_1(self):
#     self.run_test(given_answer=['S', 'N', 'Y'], expected_print='Welcome to Python Pizza Deliveries!\nYour final bill is: $16.\n')
#
#   def test_2(self):
#     self.run_test(given_answer=['L', 'N', 'N'], expected_print='Welcome to Python Pizza Deliveries!\nYour final bill is: $25.\n')
#
#   def test_3(self):
#     self.run_test(given_answer=['M', 'Y', 'N'], expected_print='Welcome to Python Pizza Deliveries!\nYour final bill is: $23.\n')
#
#
# print('\n\n\n.\n.\n.')
# print('Checking if your print statements match the instructions. \nFor a small pepperoni pizza with extra cheese your program should print this line *exactly*:\n')
# print('Your final bill is: $18.\n')
# print('\nRunning some tests on your code with different pizza combinations:')
# print('.\n.\n.')
# unittest.main(verbosity=1, exit=False)
#
# os.remove('testing_copy.py')