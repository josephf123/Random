start = int(input("Choose where the semiprimes will start: "))
final = int(input("Choose where the semiprimes will go up to: "))

prime = True

primeNum = []

semiPrimeNum = []

startVal = 0

endVal = 0


#Finds all the primes within the range of the input 'where will it go up to' and it excludes 1 and the last number
for x in range(2, final):
    for y in range(2, x):
        # if the x value divided by the y value is the same as the rounded answer of it, it means that x is NOT prime
        if x/ y == round(x/y):
            prime = False
    #if x is prime, it is added to an array of all the prime numbers
    if prime == True:
        primeNum += [x]
    #This resets the prime evaluator
    prime = True

#This finds all the semi prime numbers by multiplying all the prime numbers together
for x in primeNum:
    for y in primeNum:
        z = x * y
        semiPrimeNum += [z]

#The set method gets rid of any duplicate numbers and the sorted method puts the array in numerical order 
semiPrimeNum = sorted(set(semiPrimeNum))

#This finds where in the array it should start
for x in range(len(semiPrimeNum)):
    if semiPrimeNum[x] > start:
        startVal = x
        break
#This finds where in the array it should end
for x in range(len(semiPrimeNum)):
    if semiPrimeNum[x] > final:
        endVal = x - 1
        break

#It prints off all the semiprime numbers from the desired range of the user
print(semiPrimeNum[startVal:endVal + 1])
