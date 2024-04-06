theme: jekyll-theme-minimal

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

invalid = '''
           ___
          (   )
          |   |
          |   |
          |   |
          |   |
        __|   |__
     __/  \  _/__\___
    /  \   |/        |
    |   |  |______    |
    |\  |  |  |  |    |
    | '-\__'  '--'   |
    \         (     /
     \             /
      |            |
'''

#Write your code below this line 👇

# Rock = 0 // Paper = 1 // Scissors = 2
# 
import random
user_choice = input("Choose your weapon. Rock / Paper / Scissors\n").lower()

if user_choice == "rock":
  user_roll = 0
elif user_choice == "paper":
  user_roll = 1
elif user_choice == "scissors":
  user_roll = 2
else:
  user_roll = 3
computer_roll = random.randint(0,2)

if user_roll == 3:
  print(invalid)
  print("Please choose properly")
else:
  user_print_roll = ["rock", "paper", "scissors"]
  user_print_index = user_print_roll.index(user_choice) 
  game_images = [rock, paper, scissors]

  print(game_images[user_print_index])
  print("Computer chose:\n")
  print(game_images[computer_roll])

  if user_roll == 0 and computer_roll == 2:
    print("You win!")
  elif user_roll == 2 and computer_roll == 0:
    print("You lose!")
  elif computer_roll > user_roll:
    print("You lose!")
  elif user_roll == computer_roll:
    print("It's a draw!")
  elif user_roll > computer_roll:
    print("You win!")
