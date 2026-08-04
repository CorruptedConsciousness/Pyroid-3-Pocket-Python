import random

while True:
     x = random.randint(1, 10)

     guess = int(input("Guess a number between 1 & 10: "))

     while guess != x:
          guess = int(input("Guess again: "))

     print("Good guess!")

     again = input("Play again? yes/no: ")
     if again == "no":
               break

     