#!/usr/bin/env python
# HW02_ex03_05

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +


# Hint: to print more than one value on a line, you can print a comma-separated
# sequence:

# print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so the 
# value printed next appears on the same line.

# print '+', 
# print '-'

# The output of these statements is '+ -'.

# A print statement all by itself ends the current line and goes to the next line.

# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body


# Make 2 boxes by 2 boxes
def two_by_two():
	do_twice(boxy, 2)
	plus_line(2)


# Make 4 boxes by 4 boxes
def four_by_four():
	do_four(boxy, 4)
	plus_line(4)


# Prints Line A then Line B 4 times
# num_boxes is how many times I need the pattern of head + tails
def boxy(num_boxes):
	plus_line(num_boxes)
	do_four(pipe_line, num_boxes)


# Line A = pattern with pluses
def plus_line(num_boxes):
	print_line(num_boxes, '+ - - - - ', '+')


# Line B = pattern with pipes
# Takes 1 parameter and sets up print_line with the arguements it needs for the pattern
def pipe_line(num_boxes):
	print_line(num_boxes, '|         ', '|')


# Takes the num_boxes and uses it to create the pattern at the right length
def print_line(repetions, head, tail):
	print(head * repetions + tail)


def do_twice(f, x): # FYI - referring to fx and giving it x
	f(x) # FYI - calling it
   	f(x)


def do_four(f, x):
	do_twice(f, x)
	do_twice(f, x)





# Write your functions above:
################################################################################
def main():
    two_by_two()
    four_by_four()
    



if __name__ == "__main__":
    main()