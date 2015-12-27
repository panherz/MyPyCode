__author__ = 'dark00ps'

# USER INPUT
# The simplest use of the input function assigns a string to a variable.

print('Please enter your name\n')
inputFirstName = input()
print('\nAnd your last name\n')
inputLastName = input()
print('\nMy full name is', inputFirstName, inputLastName, '\n')

# The input function only produces strings.
# One can use the int funtion to convert a properly formed string of digits into an interger

print('Please enter a number\n')
inputNumber = input()
print('The number entered is', inputNumber, '\n')
myNumber = int(inputNumber)
print('The user input string', inputNumber, 'is now an interger as can be confirmed by the type here:David', type(myNumber), '\n')

# Calculations can also be done based on user input.
totalCount = myNumber * myNumber
print('The number inputed multiplied by itself =', totalCount, '\n')

# You can also combine input and int functions into one statement(technique known as functional composition).
int(input('Please enter a number.\n'))

# EVAL FUNCTION
# Input from a user produces a string.
# That input can be treated as a number.

myNumber = int(input('\nPlease enter a number\n.'))
print('The user input has now been converted into a number with the value of', myNumber, 'of type', type(myNumber), '\n')

# What if we wish x to be of type integer is the user enters 2 and x to be a floating point if the user enters 2.0
# The eval function can attempts to evaluate the string thee same way that an interactive shell would evaluate it.

evalX1 = eval(input('\nEnter evalX1:'))
print('evalX1 = ', evalX1, 'which has type:', type(evalX1), '\n')