num = input("Pick a number that the fibonacci sequence will go up to: ")

a = 1

b = 0

error = False

#This checks if the input of the user is a number not a string
if int(num) is num:
    error = True
#This checks if the input of the user is a number greater than 0
if int(num) < 0:
    error = True
if error == True:
    num = input("Please enter a valid number: ")

if error == False:
    #While "a" is less than the number specified by the user, it will print "a"
    while a <= int(num):
        print(a)
        b = a - b
        a = a + b
