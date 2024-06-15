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

players_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

#computer generates a random integer between 0 and 2 for their choice
computers_choice = random.randint(0,2)
