alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
's','t','u','v','w','x','y','z']
phrase = input("Enter phrase that you want encoded/decoded: ").lower()

key = input("Enter the key you want to use: ").lower()

code = input("Enter 'E' to encode the phrase and 'D' to decode the phrase ")


#The numeric value of the letters of the phrase and key, in that order
#The numeric value of a letter is how many letters are before it. E.G The numeric value of "A" is 0, "B" is 1 etc.
num = []


#Final value of the key + the phrase
final = ""


#The coded answer (if the user chooses that)
coded = []

#The decoded answer (if the user chooses that)
decoded = []

counter_spaces = 0

combined = phrase + key

error = False

spaces = []
#If any value that isn't in the alphabet is inputed it will ask to enter a valid phrase/key
for i in combined:
    if i.lower() not in alphabet:
        if i != " ":
            error = True

for i in range(len(phrase)):
    if phrase[i] == " ":
        spaces += [i]


phrase = phrase.replace(" ", "")


if error == True:
    print("Please enter valid characters!")
    phrase = input("Enter phrase that you want encoded/decoded: ")
    key = input("Enter the key you want to use: ")


################################################################################################


#newKey is the new key which has the same amount of characters as the phrase
#For example if the phrase is "jeopardized" and the key is "bat" the newKey would be "batbatbatbatba" so now the key is as long as the phrase
newKey = key


#Adds the key to itself until it is close to the amount of characters in the phrase
while len(phrase) >= len(newKey):
    if len(newKey) + len(key) > len(phrase):
        break 
    newKey += key
#Gets the key to fully equal the phrase in length by adding each letter individually   
for i in range(len(phrase) % len(newKey)):
    newKey += newKey[i]

################################################################################################

#finds the numeric value of each letter in the phrase and adds it to an array
for y in phrase:
    for r in range(len(alphabet)):
        if alphabet[r] == y:
            num += [r]

#finds the numeric value of each letter in the new key and adds it to an array
for x in newKey:
    for i in range(len(alphabet)):
        if alphabet[i] == x:
            num += [i]

################################################################################################
if code.lower() == "e":
    #adds the nth letter of phrase with nth letter of key
    for i in range(len(phrase)):
        coded += [int(num[i]) + int(num[len(phrase) + i])]
    #if the value of two letters added together is above 26, get the modulus of it
    for i in range(len(coded)):
        if coded[i] > 25:
            coded[i] = (coded[i] % 26)
        coded[i] = alphabet[coded[i]]
    #join the array with "" to become one word    
    final = "".join(coded)

################################################################################################

if code.lower() == "d":
    #subtracts the nth letter of phrase with nth letter of key
    for i in range(len(phrase)):
        decoded += [int(num[i]) - int(num[len(phrase) + i])]
    #if the value of two letters subtracted from each other is below 26, get the modulus of it
    for i in range(len(decoded)):
        if decoded[i] > -25:
            decoded[i] = (decoded[i] % 26)
        decoded[i] = alphabet[decoded[i]]
    #join the array with "" to become one word  
    final = "".join(decoded)


#################################################################################################

def add_space(string, index):
    string = string[:index] + " " + string[index:]
    return string

for x in spaces:
    final = add_space(final, x)

#Prints the encoded/decoded word
print(final, "this is the decoded/encoded message")



