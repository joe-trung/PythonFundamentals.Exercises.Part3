from random import randrange
user_input = int(input("Please enter your number from 1 to 10:"))
random_number = randrange(10)
if user_input==random_number:
    print("Good job")
elif user_input<random_number:
    print("Your number is too small")
else:
    print("Your number is too big")