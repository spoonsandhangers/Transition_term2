# while loops
# repeats until a condition is met
# we use theseloop swhen we are not sure how many times
# we want the code to repeat.

# a condition is something that will equate to either true or false.

# starter
# What is the output of this code?

# myNum = 0
#
# while myNum > 0:
# 	print("Hello")
# 	myNum + 1

# a while loop will run infinitely unless the condition
# eventually becomes false.

# counts back from 10
# count = 10
#
# while count > 0:
# 	print(count)
# 	count -= 1

# can used for validation
# This loop has no count value so will carry on
# running until the user guesses the name
# correctly

# name = "bob"
# guess = True
#
# while guess:
# 	userGuess = input("Guess my name")
# 	if name == userGuess:
# 		print("Well done you guessed it!")
# 		guess = False


### activities #####

# look at the code shown
# There is variable called password set at "let me in"
# and a variable called access set to True
# write a while loop that asks the user for their password and stores it in a variable
# called userPass.
# if the password matches the password stored in the variable password
# print a message and set access to False, this should stop the loop running.
# if the password does not match continue to ask the user to enter their password.
#
# password = "let me in"
# access = True
#
# while access:
# 	userPass = input("Enter your password")
# 	if password == userPass:
# 		print("Access granted!")
# 		access = False
# 	else:
# 		print("Access denied!")


# create another variable to count the number of times the user
# gets the password wrong.
# print this out once access has been granted.

# password = "let me in"
# access = True
# count = 0
#
# while access:
# 	userPass = input("Enter your password")
# 	if password == userPass:
# 		print("Access granted!")
# 		access = False
# 		print("You had", count, "attempts at the password")
# 	else:
# 		print("Access denied!")
# 		count += 1


# Only give the user 3 guesses then deny them access.

# password = "let me in"
# access = True
# count = 0
#
# while access:
# 	userPass = input("Enter your password")
# 	if password == userPass:
# 		print("Access granted!")
# 		access = False
# 		print("You had", count, "attempts at the password")
# 	else:
# 		print("Access denied!")
# 		if count == 2:
# 			access = False
# 			print("You have had the maximum amount of guesses", count + 1)
# 		count += 1


# set the value of a variable secretNum to an integer.
# ask the user to guess the number
# while the user guess is not the same as the secret number
# keep letting the user guess
# when the user guesses correctly print out a message
# and stop asking for a guess

# secretNum = 11
# guessed = True
#
# while guessed:
# 	userGuess = int(input("Enter an integer to guess the secret number:"))
# 	if userGuess == secretNum:
# 		print("You've guessed it!")
# 		guessed = False

# give the user a hint
# Let them know if their guess is more or less than the secret number
# only give them 5 guesses.

# secretNum = 11
# guessed = True
# tries = 0
# maxTries = 5
#
# while guessed:
# 	userGuess = int(input("Enter an integer to guess the secret number:"))
# 	if userGuess == secretNum:
# 		print("You've guessed it!")
# 		guessed = False
# 	elif userGuess > secretNum:
# 		print("You've guessed higher than the number.")
# 	elif userGuess < secretNum:
# 		print("You've guessed lower than the number.")
# 	tries += 1
# 	if tries == maxTries:
# 		guessed = False
# 		print("you've had the maximum number of guesses!")


# assign dice rolls to a variable
# while the total dice roll is lower than 21 keep rolling
# once the dice roll is over 21 tell the user their total and
# how many times they rolled

import random

dice_rolls = 0
turn = True
count = 0

while turn == True:
    roll = random.randint(1,6)
    dice_rolls = dice_rolls + roll
    count += 1
    print(dice_rolls, " is the total of all the dice rolls.")
    if dice_rolls >= 21:
        turn = False
        print("You rolled:", count, "times.")


# stretch and challenge
# turn this into a player against the computer game
# let the user roll first and see how many rolls it takes them to
# score more than 21
# Then have the computer roll
# The person who rolls the least amount of times wins or if they
# are the same the person who is also closest to 21.

