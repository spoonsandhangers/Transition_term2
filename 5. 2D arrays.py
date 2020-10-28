"""
2D arrays are arrays of arrays
of lists of lists in Python
"""
# starter
# what will this print out?

menu = [["eggs","bacon","beans","toast"],["vegetable soup","bread roll"],["cottage pie", "carrots","gravy"]]

print("The menu for breakfast is:")
for i in range(len(menu[0])):
	print("*", menu[0][i])

# menu[0] references the first item in the menu list
# this item is the list containing "eggs","bacon","beans","toast"
# menu[0][0] references the first element in this list "eggs"

# can you print out the lunch menu in the same way?

# Add a dessert menu to the menu list containing 3 desserts
# show how you would print out the 2nd dessert item in the list.
# print out the whole menu with headings inbetween the courses.

# extension
# create a list called exercises that contains 3 separate lists
# the 3 lists should be arm, leg and abdominal exercises.
# there should be 3 of each exercise.
# ask a user which workout they would like
# print out that list in a bulleted format
# extension 2 - let the user also choose a mixed workout
# this should select one exercise from each list

# you can also represent a 2D array like this

summer = ["june","july","august"]
autumn = ["september","october","november"]
winter = ["december","january","february"]
spring = ["march","april","may"]

year = [spring, summer, autumn, winter]

print(year[1][0])



