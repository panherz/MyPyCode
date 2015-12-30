# PRINT FUNCTION

# Make cursor remain at the end of the printed line.
# (Not working yet) print('Please enter value and the cursor remains at end:\n', end='')

w, x, y, z = 5, 10, 15, 20
print(w, x, y, z)

print(w, x, y, z, sep=',')

print(w, x, y, z, sep='')

print(w, x, y, z, sep='-----------------')

x = 6
print(6)
print("6")
print('x')

print('\nA\nB\nC\nD\nE\nF\n')
print('\a')

"""
ces. For a simple example, here's some python code from the blender build scripts:

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

To use code like this, you can do something like

print bcolors.WARNING + "Warning: No active frommets remain. Continue?"
      + bcolors.ENDC

This will work on unixes including OS X, linux and windows (provided you enable ansi.sys). There are ansi codes for sett
ing the color, moving the cursor, and more.

If you are going to get complicated with this (and it sounds like you are if you are writing a game), you should look
into the "curses" module, which handles a lot of the complicated parts of this for you. The Python Curses HowTO is a good introduction.

"""


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(bcolors.OKGREEN + "Warning: No active frommets remain. Continue?"
      + bcolors.ENDC)
