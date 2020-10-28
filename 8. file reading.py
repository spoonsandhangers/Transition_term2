"""
reading files in python
files must be in same folder as python file
or specify the path
"""

#starter

# myFile = open("films1.txt", "r")
#
# fileRead = myFile.readlines()
#
# for line in fileRead:
# 	print(line, end="")
#
# myFile.close()

# alternative code
# for line in myFile.readlines():
#     print(line, end = "")

######## activity ############
# Fix the code provided below so
# that you can read the file whoswho.txt

# myFile = open()
#
# fileRead =
#
# for
# 	print()
#
# myFile.

################# activity #############

# read the file cats1.txt
# print out the contents line by line.

# myfile = open("cats.txt", "r")
#
# fileRead = myfile.readlines()
#
# for line in fileRead:
# 	print(line, end="")
#
# myfile.close


######## activity ##############
# this code takes the file films1 and prints it out in a user friendly way
# modify this code so that you can read the file fanDetails.txt
# Make the titles of the fields e.g. film title fit the information in the new file.

# myFile = open("films1.txt", "r")
#
# fileRead = myFile.readlines()
#
# for line in fileRead:
# 	fileList = line.split(",")
# 	for i in range(len(fileList)):
# 		if i == 0:
# 			print("* Film title:", fileList[i], end=' * ')
# 		elif i == 1:
# 			print("Film certificate:", fileList[i], end=' * ')
# 		else:
# 			print("Year of filming:", fileList[i])
#
# myFile.close()
