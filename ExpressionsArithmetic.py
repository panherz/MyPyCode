# EXPRESSIONS & ARITHMETIC

# Arithmetic Operations
# +++++++++++++++++++++
# Common ones are ok + - / ete etc
# Others include //is used for integer division and the % is the modulus or remainder operator
# Another is += (same as x = x + 1) or -= (same as x = x - 1)
# Another short one would be x +=5 (adds or minus's 5  to x)

salesman = str(input('What is the salesman\'s name?\n'))
saleswoman = str(input('What is the saleswoman\'s name?\n'))

# value1 = eval(input('Enter the total sales for', salesman, '?\n'))
# value2 = eval(input('Enter the total sales for', saleswoman, '?\n'))
# total = value1 // value2

# The above doesn't work but the below does.
# value1 = eval(input('Enter the total sales for', salesman, '?\n'))
# TypeError: input expected at most 1 arguments, got 3

# You should use format to build the string
#       cake_amnt = int(input('How many {} would you like to make?'.format(cake)))
#       Or use the + operator to perform concatenation
#       cake_amnt = int(input('How many ' + cake + ' would you like to make?'))

value1 = eval(input('Enter the totals sales for ' + salesman + '?\n'))
# A user can also enter 23 + 4
value2 = eval(input('Enter the total sales for {}?\n' .format(saleswoman)))
total = value1 + value2

# If you want to put several Python statements on the same line, you can use a semi-colon to separate them.

print('The total sales for', salesman, 'and', saleswoman, '\n')
print('EQUALS\n')
print('$', total, sep='')

"""
    This is a multi line comment
    Understood
    """
