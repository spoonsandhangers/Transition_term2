# # Starter
# # What is the output of this code?
#
# m = int(input("Enter a number: "))
#
# print("1 X", m, "=", m * 1)
# print("2 X", m, "=", m * 2)
# print("3 X", m, "=", m * 3)
# print("4 X", m, "=", m * 4)
# print("5 X", m, "=", m * 5)
# print("6 X", m, "=", m * 6)
#
# # Examples of For loops
#
# #prints hello 10 times
# for i in range(10):
# 	print("Hello")
#
# # prints 0 to 9 on new lines
# for i in range(10):
# 	print(i)
#
# # prints 1 to 9 on new lines
# for i in range(1, 10):
# 	print(i)
#
# # prints 1 to 10 on new lines
# for j in range(1, 11):
# 	print(j)
#
# # prints in steps of 2 starting with 1
# # so all the odd numbers between 1 and 10.
# # all on separate lines
# for s in range(1, 11, 2):
# 	print(s)


# ############ activities ########## #

# write an algorithm that asks the user for their name
# uses a for loop to print out "Hello" and their name 10 times.
name = input("Enter yor name: ")

for i in range(10):
	print("Hello", name)


# write a for loop that displays the numbers 10 to 100 in steps of 5
# make sure it includes 10 and 100
for i in range(10, 101,5):
	print(i)


# Write a loop that displays the 5 times table from 1 to 12 in the following format
# 1 x 5 = 5
# 2 x 5 = 10 etc.
# You are only allowed to use 1 print statement.

for i in range(1, 13):
	print(i, "x 5", "=", i * 5)

# extension
# ask the user for a number and print out the multiplication
# table for that number up to 12.
userNum = int(input("Enter an integer: "))

for i in range(1, 13):
	print(i, "x", userNum ,"=", i * userNum)

########### Example #############

# using the in keyword you can iterate through a string or list
phrase = "Spinning around in circles"

for char in phrase:
	print(char)

# extension
counti = 0
for char in phrase:
	if char == "i":
		counti = counti + 1

print("The number of i's is:", counti)

# char is the loop variable, instead of being set ot a number each time the loop
# executes it is set to the next character in the string.

####  activities #######

# ask the user for a sentence, assign this to a variable
# use a for loop to count the number of e's in the sentence and print out the result.

sentence = input("Enter a sentence: ")

eCount = 0

for i in sentence:
	if i == "e":
		eCount += 1

print("The sentence has:", eCount, "e's")

## extension ##
# a break statement stops the loop executing immediately.
# example:

for i in range(10):
	if i == 8:
		print("reached the number 8")
		break

# this for loop will stop once it reaches the number 8

# write a for loop that will ask the user for a sentence and
# count the number of e's and print out the total
# if it gets to the letter 'n' it must stop immediately and print out the total number of e's up to that point.
# test it on the sentence "the cat sat on the mat"


sentence = input("Enter a sentence: ")

eCount = 0

for i in sentence:
	if i == "n":
		break
	elif i == "e":
		eCount += 1

print("The sentence has:", eCount, "e's")

# Go onto for loop challenge sheet.




