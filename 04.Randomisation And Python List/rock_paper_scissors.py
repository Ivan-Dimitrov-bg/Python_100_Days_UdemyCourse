import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissors]

user_choice = input("Plelase chouse, rocke = 0, paper = 1, scissors = 2")

computer_choice = random.randint(0, 2)

print(game_image[user_choice])
print("Computer chose:")
print(game_image[computer_choice])

if user_choice < 0 or user_choice > 2:
  print("you enter a wrong number")
elif(user_choice == 0 and computer_choice == 2):
  print("you win")
elif(user_choice == 0 and computer_choice == 1):
  print("you lose")
elif(user_choice < computer_choice):
  print("you lose")
elif(user_choice > computer_choice):
  print("you win")
elif(user_choice == computer_choice):
  print("it is a draw")