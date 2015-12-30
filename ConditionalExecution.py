# CONDITIONAL EXECUTION

# Boolean...simply true or false

# Python considers zero to be false and so wih strings '' or ""

# x == y, X < y. x <= y, x > y, x <= y, x! = y

# x + 2 < y / 10 is evaluated as (x + 2) < (y / 10)

# dividend, divisor = eval(input('Please enter two numbers to divide:\n'))

# print('Number entered: ', dividend, ' and ', divisor)

# If possible, divide them and report the result
# if divisor != 0:
#    print(dividend, '/', divisor, '=', dividend/divisor)

# A block is a block of one or more statements to be executed if the condition is true.
# Indentation in python determines which statement make a block

# Request input from user
num = eval(input('Please enter an integer between 0 .... 9999:\n'))

# Attenuate the number is necessary
if num < 0:  # Make sure number is not too small
    num = 0
if num > 9999:  # Make sure number is not too big
    num = 9999

print(end='[\n')

# The if else statement

myNum = eval(input('Please enter a number between 0 and 9999\n'))

if myNum == 41:
    print(myNum, 'See the Doctor\n')

else:
    print(myNum, 'run boy\n')

    # Simple Boolean expressions, each involving one relational operator, can be combined into more complex
    # Boolean expressions using the logical operators and, or, and not. A combination of two or more Boolean
    # expressions using logical operators is called a compound Boolean expression.
