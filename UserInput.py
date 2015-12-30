__author__ = 'dark00ps'

# USER INPUT
# The simplest use of the input function assigns a string to a variable.

print('Please enter your first name::::\n', end='')
inputFirstName = input()
print('\nAnd your last name::::\n')
inputLastName = input()
print('\nMy full name is::::', inputFirstName, inputLastName, '\n')

# The input function only produces strings.
# One can use the int function to convert a properly formed string of digits into an integer

print('Please enter a number:::::\n')
inputNumber = input()
# print('The number entered is', inputNumber, '\n')
myNumber = int(inputNumber)
print('The user input string', inputNumber, 'is now an integer as can be confirmed by the type here:', type(myNumber), '\n')

# Calculations can also be done based on user input.
totalCount = myNumber * myNumber
print('The number entered multiplied by itself =', totalCount, '\n')

# You can also combine input and int functions into one statement(technique known as functional composition).
xxxx = int(input('\nPlease enter a string that will be turned into type int::::\n'))
print('\nThe int value of xxxx is:', xxxx, '\n')

# EVAL FUNCTION
# Input from a user produces a string.
# That input can be treated as a number.

myNumber = int(input('\nPlease enter a number to be converted::::\n'))
print('The user input has been converted into a number with the value of', myNumber, 'of type', type(myNumber), '\n')

# What if we wish evalX1 to be of type integer when the user enters 2 and evalX1 to be a floating point if the user
# enters 2.0
# The eval function can attempts to evaluate the string the same way that an interactive shell would evaluate it.

evalX1 = eval(input('Enter number you would wish to be evaluated::::\n'))
print('evalX1 = ', evalX1, 'which has type:', type(evalX1))

# Set the type of variable before user input

inputAnyNumber = float(input('\nPlease enter a floated number::::\n'))
print('\nThe number entered is now floated:', inputAnyNumber, '\n')

inputAnyNumber = int(input('\nPlease enter an int::::\n'))
print('\nThe number entered is now an int:', inputAnyNumber, '\n')

# Evaluate 2 Inputs from a user

num1, num2 = eval(input('Please enter number 1, and a number 2 making use of a comma::::\n'))
print("The total for number 1 and number 2 is", num1 + num2, '\n')

print(eval(input('Enter anything')))