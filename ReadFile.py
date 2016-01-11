# Program to read file
userInput = raw_input('What file do you want to read')
myfile = open(userInput)
# myfile = open('/home/dk/readfile.txt')
info = myfile.readlines()
print info
myfile.close()

