import random
user_choice=int(input("what do you choose? type 0 for rock ,1 for paper or 2 for scissor"))
list=["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""","""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)  """ ,"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
print(list[user_choice])
print("computer choose")
computer_choice=random.randint(0,2)
print(list[computer_choice])
if(user_choice==computer_choice):
  print("match draw")
elif((user_choice==1 and computer_choice==2) or(computer_choice==1 and user_choice==0)):
  print("computer wins")
else:
  print("you win")
