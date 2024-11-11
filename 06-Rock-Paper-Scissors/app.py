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

user_input = int(input('What do you choose? Type "0" for Rock, "1" for Paper or "2" for Scissors.\n'))
if user_input == 0:
    print('You chose: "Rock"')
elif user_input == 1:
    print('You chose: "Paper"')
elif user_input == 2:
    print('You chose: "Scissors"')
game_option = [rock, paper, scissors]
print(game_option[user_input])

computer_input = random.randint(0, 2)
if computer_input == 0:
    print('Computer chose: "Rock"')
elif computer_input == 1:
    print('Computer chose: "Paper"')
elif computer_input == 2:
    print('Computer chose: "Scissors"')

print(game_option[computer_input])

if user_input == computer_input:
    print("It's a draw!")
elif (user_input == 0 and computer_input == 2) or \
     (user_input == 2 and computer_input == 1) or \
     (user_input == 1 and computer_input == 0):
    print("You Win!")
else:
    print("You Lose!")
