__author__ = 'dark00ps'

# Printing

var = 'This is how you print in Python 3'

print(var)

print('This is another way')

# Styling Print

print('     *      ')
print('    ***     ')
print('   *****    ')
print('  *******   ')
print(' *********  ')
print('     *      ')
print('     *      ')
print('     *      ')
print('     *      ')


# Types (Determine the type)

print(type(4))
print(type('Is this a string'))
print('Fred')

# Variables

counter = 77777777           # An integer assignment
miles = 88888.0          # A floating point
name = 'John'           # A string


# Multiple Assignment

a = b = c = 99999
print(a)

a, b, c, = 1000, 2000000, 'John'
print(a)
print(b)
print(c)

# Data Types
# Python has five standard data types
# http://www.tutorialspoint.com/python/python_variable_types.htm
# Numbers, Stings, Tuple, Dictionary
# You can also delete a single object or multiple objects i.e del var1, del var1,var2

print(counter)
del counter
# print(counter)          # Will return an error as variable has been deleted.

# Strings

varString = str('12 Hazelwood Close')
print(varString)
varString = 5 + 10
print(varString)
varString = ('5' + '10')
print(varString)
# varString = (5 + (str=10))
print(varString)

# Line Breaks

varString = str('Go to \n ****HELL****\n')
print(varString)

varString2 = str('Hurray')
# print(varString2('\n\n'))

varString = str('Did line break work?')
print(varString)