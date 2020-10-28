"""
Timetable challenge
"""

# declare 5 arrays called monday, tuesday, wednesday, thursday and friday
# each array should store the lessons that you have that day in order
# any free periods should store the string "free"
# declare an array called week
# store all the days of the week in order in this array

# design an algorithm that
# asks the user what day and what period they want to look at
# prints out the lesson that is timetabled for that period
# e.g. monday period 3 = design
monday = ["free", "python","employability","free"]
tuesday = ["python", "web design","english","free"]
wednesday = ["maths","python","english","employability"]
thursday = ["web design","graphic design", "free","maths"]
friday = ["free","maths","python","free"]

week = [monday, tuesday,wednesday,thursday,friday]

day = int(input("Enter the day of the week as a number 1 to 5:"))
period = int(input("Enter the period 1 to 4: "))

print("The timetabled lesson is:", week[day-1][period-1])

# extension - add a menu so that the user can choose to pick a lesson
# or quit the system, after each choice.

# extension add a menu option so that a user can change the timetabled lessons



