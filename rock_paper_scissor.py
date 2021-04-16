# Rock Paper Scissors
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
game_images = [rock, paper, scissors]
player_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("Your Move: ")
print(game_images[player_move])

computer_move = random.randint(0, 2)
print("Computer's Move")
print(game_images[computer_move])

if player_move == 0 and computer_move == 2:
    print("You Won")
elif computer_move == 0 and player_move == 2:
    print("Computer Won")
elif player_move == 2 and computer_move == 1:
    print("You Won")
elif computer_move == 2 and player_move == 1:
    print("Computer Won")
elif player_move == 1 and computer_move == 0:
    print("You Won")
elif computer_move == 1 and player_move == 0:
    print("Computer Won")
elif computer_move == player_move:
    print("Tie")
