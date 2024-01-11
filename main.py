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
print("Welcome to the Rock, Paper, Scissors Game!")
user_input=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
arr= [rock, paper, scissors]
if user_input == "0":
  print(rock)
elif user_input == "1":
  print(paper)
else:
  print(scissors)

com=random.randint(0,2)
print(com)

if user_input == "0" and com == 0:
  print(rock)
  print("Draw")
elif user_input== "0" and com == 1:
  print(paper)
  print("You lose")
elif user_input=="0" and com == 2:
  print(scissors)
  print("You win")
elif user_input=="1" and com == 0:
  print(rock)
  print("You win")
elif user_input=="1" and com == 1:
  print(paper)
  print("Draw")
elif user_input=="1" and com == 2:
  print(scissors)
  print("You lose")
elif user_input=="2" and com ==0:
  print(rock)
  print("You lose")
elif user_input=="2" and com == 1:
  print(paper)
  print("You win")
else:
  print(scissors)
  print("Draw")
  