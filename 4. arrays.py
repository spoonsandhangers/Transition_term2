"""
An array in computer science is usually
described as a fixed length data structure that stores elements of
one data type, it cannot contain duplicate elements.
In Python the commonly used data structure is called a list and
is more similar to a vector.
It expands to fit as many elements as required during runtime, stores
elements of different data types and also can contain duplicate elements.
"""

armExercises = ["bicep curl", "lateral raise", "tricep extension", "dumbell row", "dumbell kickback"]
legExercises = ["squat", "reverse lung", "side lung", "dead lift","calf raise" ]

# for i in armExercises:
# 	print(i)

# can you modify this code using previous for loop knowledge so that you can make a numbered list
# that look like this:
# 1. bicep curl
# 2. lateral raise etc.
# You can find the length of a list using the same function
# you use with Strings len()

# length = len(armExercises)
# print("The arm exercises list length is:", length)

# # answer simple
# for i in range(len(armExercises)):
# 	print(i, ".", armExercises[i])
#
# # answer better
# for i in range(len(armExercises)):
# 	bullet = str(i) + "."
# 	print(bullet, armExercises[i])

# Elements in a list have an index value the same as a string
# this starts at 0
# in the armExercises list "bicep curl" is at index 0
# "tricep extension" is at index 2

# print("The best arm exercise is:", armExercises[0])

# We can change the elements in a list by using this way of addressing them

# armExercises[4] = "front raise"
#
# print("Element 4 is now:", armExercises[4])

# An error will occur if you try to change an element that is
# beyond the size of the list.

# You can add an element to the end of the list using append()

# armExercises.append("push up")
# print(armExercises)

# Add 2 more leg exercises to the legExercise list
# Your own or "goblet squat" and "hack squat"

# legExercises.append("goblet squat")
# legExercises.append("hack squat")

# imagine you are a personal trainer and you want to
# print out a workout for a client
# You want them to do 12 reps of each arm and leg exercise
# in the list.
# They should be printed like this:
# 12 x bicep curl
# 12 x lateral raise
# etc.

# for i in armExercises:
# 	print("12 x", i)
#
# for i in legExercises:
# 	print("12 x", i)

# This isn't very user friendly
# add some more print statements to specify when the arm and leg exercises start
# You would like to set the number of reps of each exercise
# differently depending on whether the client
# wants to bulk up or just tone
# write an algorithm that asks the client if they want to
# put on muscle or just tone.
# if they want to put on muscle print:
# You have chosen to gain muscle
# choose a heavy weight and complete:
# 6 x bicep curl
# 6 x tricep extension etc.
# if the user chooses tone then they
# should choose a lower weight and complete 12 reps.
#
# choice = input("Enter 'm' for gain muscle or 't' for tone")
#
# for i in range(len(armExercises)):
# 	if choice == "m":
# 		print("6 x", armExercises[i])
# 	else:
# 		print("12 x", armExercises[i])

# write a subroutine that prints out the arm exercises
# when called along with the number of reps
# required.
# extension - pass the number of reps as a parameter

# def arm(reps):
# 	for i in armExercises:
# 		print(reps, "x", i)
#
# arm(12)

# slicing a list
# we can find part of the list and make a copy of it
# This prints from index 0 up to but not including index 3.

# print(armExercises[0:3])

# try out these list slices and see what they do:

# print(armExercises[:2])
# print(armExercises[2:])
# print(armExercises[:])

# we can choose a random element from a list by importing
# choice from the random library
# from random import choice
#
# print(choice(armExercises))

# design an algorithm that
# asks the user if they want a leg or arm exercise
# picks a random exercise form the correct list and
# prints it out.
# if the choice isn't either of those it prints out that
# the choice is invalid

# from random import choice
#
# userExercise = input("Would you like a leg or arm exercise? select 'a' or 'l' ")
# if userExercise == "l":
# 	print(choice(legExercises))
# elif userExercise == "a":
# 	print(choice(armExercises))
# else:
# 	print("That was not a valid choice")



# make a new list that contains the days of the week
# use a for loop to look at each day one at a time
# print out "Today is" and the day of the week for each day
# if it is a weekday also print out "Get up early"
# if it is a weekend day also print out "Yay it's the weekend"
#
# daysOfWeek = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
#
# for i in daysOfWeek:
# 	print("The day is: ", i)
# 	if i == "monday" or i == "tuesday" or i == "wednesday" or i == "thursday" or i == "friday":
# 		print("Get up early!")
# 	else:
# 		print("Yay it's the weekend!")

# change the code so that it now picks a random day from the
# days of the week and prints out whether to get up early or
# whether its the weekend.

# make an empty list called user numbers
# ask a user to enter 10 numbers one at a time and
# each time add them to the list
# go through the list and add up the numbers
# calculate the average of these numbers by dividing the total by 10
# tell the user the average of their numbers.

userNumbers = []

for i in range(10):
	userNum = int(input("Enter a number for the list: "))
	userNumbers.append(userNum)

total = 0

for i in userNumbers:
	total += i

print("The average of your numbers is:", total/10)

# extension - only add up the numbers that are even
# and find their average

#
# Loops can be nested inside each other






