##
# Exercise 1
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that
# they will turn 100 years old.
#
# Note: for this exercise, the expectation
# is that you explicitly write out the year (and therefore be out of
# date the next year). If you want to do this in a generic way, see
# exercise 39.
#
# Extras:
# 1. Add on to the previous program by asking the user for another
# number and printing out that many copies of the previous message.
# (Hint: order of operations exists in Python)
#
# 2. Print out that many copies of the previous message on separate lines.
# (Hint: the string "\n is the same as pressing the ENTER button)
##
import datetime


#age = int(input("What is your age? "))

#anum = int(input("What's a number? "))
today = datetime.datetime.today()
print(today.year, today.month, today.day)

