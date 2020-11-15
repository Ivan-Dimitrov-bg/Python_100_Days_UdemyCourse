#from replit import clear
#HINT: You can call clear() to clear the output in the console.

#import art

#print(logo)

is_it_end = False
all_bits = {}
def ask_for_name(all_bits):
  name_participant = input("Please enter your name: ")
  bit = input("Please enter your bit: ")
  all_bits[name_participant] = bit

def print_bigest_bit(all_bits):
  biggest_bit = 0
  name_winer = ""
  for name in all_bits:
    if int(all_bits[name]) > biggest_bit:
      biggest_bit = int(all_bits[name])
      name_winer = name
  print(f"The winner is {name_winer}, score: {biggest_bit}")
more_people = "y"  

while not is_it_end:

  if more_people == "y":
    #clear();
    ask_for_name(all_bits)
  else:
    print_bigest_bit(all_bits)
    is_it_end = True

  more_people = input("Do you have more people to participate?  y/n  \n")