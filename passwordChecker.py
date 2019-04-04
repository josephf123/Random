password = input("Enter a password: ")

count = 0

alphabet = "abcdefghijklmnopqrstuvwxyz "

numbers = "1234567890"

symbols = "$#-_&%"

wrongSymbol = False

symbolsIn = False

numbersIn = False

whitespace = False

countLower = 0

error_message = []


#For every character in the user's input
for x in password:
    #It counts how many characters are in the password
    count += 1
    #If there are whitespaces, the whitespace boolean will be true
    if x == " ":
        whitespace = True
    #If there is a wrong character or not enough characters, wrong symbol will turn true    
    if x.lower() not in alphabet and x not in symbols and x not in numbers:
        wrongSymbol = True
    #This counts how many lowercase letters are in the password    
    if x.lower() == x:
        countLower += 1
    #This checks if there are any symbols in the password
    for y in symbols:
        if y == x:
            symbolsIn = True
    #This checks if there are any numbers in the password        
    for i in numbers:
        if i == x:
            numbersIn = True

    


if count < 8:
    error_message += ["Your password must be over 8 characters"]
#If the amount of lowercase characters is equal to the amount of characters that means there are no uppercase letters   
if countLower == count:
    error_message += ["You need at least one captial letter"]
if whitespace:
    error_message += ["You had whitespaces in text"]
if wrongSymbol:
    error_message += ["You had an invalid symbol"]
if symbolsIn == False:
    error_message += ["You need at least one valid symbol"]
if numbersIn == False:
    error_message += ["You need at least one number"]


#If there are no errors
if error_message == []:
    print("Your password is valid")
    if count < 10:
        print("Weak strength")
    elif count < 12:
        print("Good strength")
    elif count >= 12:
        print("Excellent strength")
#If there are errors it will not print how weak or strong the password is        
else:
    print(error_message)

