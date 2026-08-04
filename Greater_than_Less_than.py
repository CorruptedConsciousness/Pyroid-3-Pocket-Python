import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
choice = random.choice(numbers)
if choice > 5:
     print(str(choice) + " is GREATER than 5.")
elif choice == 5:
	print("Its's a PUSH!!")
else:
	print(str(choice) + " is LESS than 5.")