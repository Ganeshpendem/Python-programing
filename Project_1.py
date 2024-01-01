import random
user_choice=int(input("Enter your choice: 0 for rock, 1 for Paper, 2 for Scissor: "))
computer_choice=random.randint(0,2)
print(f"The Computer choice is {computer_choice}")
print(f"The user choice is {user_choice}")

if user_choice>3 or user_choice<0:
    print("You have entered Wrong input please check the input")
elif user_choice==computer_choice:
    print("Draw the Match")
elif user_choice == 0 and computer_choice == 2:
    print("you are Win")
elif user_choice == 2 and computer_choice == 0:
    print("You are lose")
elif user_choice>computer_choice:
    print("you are wins")
elif computer_choice>user_choice:
    print("You are lose")

