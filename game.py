from random import randint

# this program demonstrates a guessing game

# get user input
user_name=input("Enter user name:")

print("hello there "+ user_name +"!")





# generate a random number
random_number=randint(10, 50)

counter=0
while counter < 6:
    user_number=eval(input("Enter a number:"))
    counter=counter +1

    if user_number < random_number:
        print("your guess is too low")
    elif user_number > random_number:
        print("your guess is too high")
    elif user_number==random_number:
        print("you won!")
        break.


# using a while loop check if user input is equal to generated number



