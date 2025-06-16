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

game_images=[rock,paper,scissors]
my_choice=int(input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Sciossors.\n"))
computer_choice = random.randint(0, 2)
if my_choice>=3 or my_choice<0:
    print("You typed a invalid number")
elif my_choice==0 and computer_choice==2:
     print(game_images[my_choice])
     print(f"computer choose{game_images[computer_choice]}")
     print("You wins")
elif computer_choice==0 and my_choice==2:
    print(game_images[my_choice])
    print(f"computer choose{game_images[computer_choice]}")
    print("You loose")
elif computer_choice >my_choice:
    print(game_images[my_choice])
    print(f"computer choose{game_images[computer_choice]}")
    print("You loose")
elif computer_choice==my_choice:
     print(game_images[my_choice])
     print(f"computer choose{game_images[computer_choice]}")
     print(" its a draw")
elif my_choice>computer_choice:
    print(game_images[my_choice])
    print(f"computer choose{game_images[computer_choice]}")
    print("You wins")


