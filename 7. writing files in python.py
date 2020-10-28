"""
writing files in python
about me file - level 1
extension - passwords and usernames.
CSV writing - level 2
"""

# starter
#
# fout = open("hello.txt", "w")
#
# fout.write("hello, world!\n")
# fout.write("hope you have a great day!\n")
#
# fout.close()
################activity#############
##### predict what this will do
# where is the file?
# what does the data in the file look like
# is it on the same line?
# How is the data separated?
# Modify the code so that it also asks for a favourite song
# this should be stored on the same line as the name and film separated with a comma
# so it looks like this for example
# bob, rocky, I will survive
# Each time you run the code the file is overwritten
# To change this change the "w" to "a"
# This is append instead of write.
# add some records
# get other people to fill it in so you have 10 records/lines

# name = input("Enter your name ")
# film = input("Enter your favourite film ")
#
# file = open("about_me.txt", "w")    #opening the text file to write in.
#
# file.write(name + ",")
# file.write(film + "\n")             #writing to the text file.
#
# file.close()                        #closing the text file.

#############activity############
# make an algorithm that:
# asks the user for a username and a password
# stores each users username and password in a text file called passwords.txt
# the username and password should be on the same line and separated by a comma
# the next time the code runs the username and password should be put on the next line

# username = input("Enter your user name: ")
# password = input("Enter your password: ")
#
# file = open("passwords.txt", "a")
#
# file.write(username + ",")
# file.write(password + "\n")
#
# file.close()

# extensions - check that the user name is more than 5 characters long
# check that the password is > 8 characters long and contains no spaces.
# keep asking the user to enter the information until the information is valid

invalid = True

while invalid:
	username = input("Enter your user name: ")
	password = input("Enter your password: ")
	if len(username) > 5:
		print("username ok")
		if len(password) > 8:
			print("password ok")
			invalid = False
		else:
			print("password not long enough!")
	else:
		print("username is too short!")

file = open("passwords.txt", "a")

file.write(username + ",")
file.write(password + "\n")

file.close()
# \n must be added if you want information to be on separate lines
# We can also use commas to separate pieces of information that we store in a file
#
# fout = open("films.txt", "w")
#
# fout.write("Back to the future, PG, 1985\n")
# fout.write("The Goonies, 12, 1985\n")
# fout.write("The karate kid, 15, 1984\n")
#
# fout.close()

# the data is organised into records
# each film is on a separate line
# each piece of information about the film is stored on one line
# and each is separated by a comma
# The information should always be in the same order
# that way when you read it back you will know what to expect.

##############example of writelines################
# uses a list and writes it to a file
# each element needs to have a new line if you want them on new lines

shoppingList = ["bread\n", "milk\n","eggs\n","biscuits\n","jam\n"]

fout = open("shopping.txt","w")

fout.writelines(shoppingList)

fout.close()

##############activity#################
###### make a to do list called myList, store the list in a file called mytodolist.txt using writelines()
# make sure each element in the list is on a new line in the file.

######### you can also use this to write 2D lists to a file.
# can you work out how this work?
# use this to write your 2D array timetable from the challenge last week to a text file called timetable.txt

# films = [["Back to the future, PG, 1985\n"],["The Goonies, 12, 1985\n"],["The karate kid, 15, 1984\n"]]
#
# fout = open("films1.txt", "w")
#
# for i in films:
# 	fout.writelines(i)
#
# fout.close()




