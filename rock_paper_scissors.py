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
---'   ____)______
          ________)
       ____________)
      (____)
---.__(___)
'''

#Write your code below this line 👇


game_images = [rock, paper,scissors]
user_choice = int(input('What do you choose? \n "0" for Rock \n "1" for paper \n "2" for sissors\n'))
if user_choice>=3 or user_choice <0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0,2)
    print("Computer chose: ")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice ==2:
        print("You Win!")
    elif computer_choice ==0 and user_choice ==2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You Win!")
    elif computer_choice == user_choice:
        print("It's a draw")