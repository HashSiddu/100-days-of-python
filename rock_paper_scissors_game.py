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
user_choice = int(input("choose any one 0 for rock 1 for paper and 2 for scissor"))
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("you entered wrong number")
#computer choice
computer_choice = random.randint(0,2) 
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)
#compare
if user_choice == 0 and computer_choice == 2:
    print("you win")
elif user_choice == 1 and computer_choice == 0:
    print("you win")
elif user_choice == 2 and computer_choice == 1:
    print("you win")
elif user_choice == computer_choice:
    print("draw")
else:    
    print("you loose")

