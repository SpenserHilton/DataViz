import random

print("Let;s play Rock, Paper, Scissors!")
options = ["r", "p", "s"]

computer_choice = random.choice(options)

user_choice = input("Make your choice: (r)ock, (p)aper, (s)cissors.")


if computer_choice == "r":
	if user_choice == "r":
		print("Draw!")
	elif user_choice == "p":
		print("You win!")
	elif user_choice == "s":
		print("Computer wins!")
elif computer_choice =="p":
	if user_choice == "r":
		print("Computer wins!")
	elif user_choice == "p":
		print("Draw!")
	elif user_choice == "s":
		print("You win!")
elif computer_choice == "s":
	if user_choice == "r":
		print("You win!")
	elif user_choice == "p":
		print("Computer wins!")
	elif user_choice == "s":
		print("Draw!")

