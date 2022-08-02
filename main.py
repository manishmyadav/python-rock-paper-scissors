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

#Write your code below this line 👇
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Scissors or 2 for Paper.\n"))

if user_choice not in [0, 1, 2]:
  print("You chose an invalid no. You lose!")

else:
  choice_list = [rock, scissors, paper]
  l1 = ['Rock', 'Scissors', 'Paper']
  computer_choice = random.choice([0, 1, 2])
  print(f"Your choice: {l1[user_choice]}")
  print(choice_list[user_choice])  
  print(f"Computer's choice: {l1[computer_choice]}")
  print(choice_list[computer_choice])

  if user_choice == computer_choice:
    print("Its a draw.")
  elif (user_choice - computer_choice == -1) or (user_choice - computer_choice == 2):
    print(f"{l1[user_choice]} wins against {l1[computer_choice]}.")
    print("You win.")
  elif (user_choice - computer_choice == 1) or (user_choice - computer_choice == -2):
    print(f"{l1[user_choice]} loses against {l1[computer_choice]}.")
    print("You lose.")

  
