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

#Write your code below this line 👇
import random

players_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

#print out the players choice
if int(players_choice) == 0:
    print(rock)
elif int(players_choice) == 1:
    print(paper)
elif int(players_choice) == 2:
    print(scissors)

#computer generates a random integer between 0 and 2 for their choice
computers_choice = random.randint(0,2)

#print out the computers choice
print("Computer chose:\n")

if computers_choice == 0:
    print(rock)
elif computers_choice == 1:
    print(paper)
elif computers_choice == 2:
    print(scissors)

#compare the choices to see who wins
if (players_choice == '0' and computers_choice == 2) or (players_choice == '1' and computers_choice == 0) or (players_choice == '2' and computers_choice == 1):
    print("You win!")
elif int(players_choice) == computers_choice:
    print("It's a draw")
else:
    print("You lose")