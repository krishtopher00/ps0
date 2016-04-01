# Number 0
def is_even(number):
    """Tests if a number is even by dividing by 2 and checking if the remainder is
    one or zero. If its 1 then the number is odd, if its 0 then the number is even"""
    if number % 2 == 1:
        return False
    elif number % 2 == 0:
        return True
        

# Number 1
def length(number):
    """Determines digits in a number by checking if the number is within the set of all numbers that have 2 digits, then 3 
    digits, then 4 digits etc."""
    numDigits = 0
    lowerBound = 1
    upperBound = 10
    while True:
        if number == 0:
            return "{} (it is a placeholder)".format(numDigits)
        else:
            numDigits += 1
            if upperBound > number >= lowerBound:
                return numDigits
            else:
                lowerBound *= 10
                upperBound *= 10
                
                
 # Number 2               
def sum_digits(number):
    """Takes a number and add all of its digits together"""
    sumNums = 0
    while number != 0:
        digit = number % 10
        sumNums += digit
        number -= digit
        number /= 10
    return sumNums
    
    
# Number 3
def sum_ints(number):
    """Takes a number and adds together all of the integers lower than it until 0"""
    sumNums = 0
    for item in range(number):
        sumNums += item
    return sumNums


# Number 4
def factorial(number):
    """Takes a number and returns that number factorialed (That number multipled by all integers lower than it until you hit 0)"""
    if number == 0:
        multipliedNumber = 1
    else:
        multipliedNumber = number
        while number != 1:
            number -= 1
            multipliedNumber *= number
    return multipliedNumber
    

# Number 5
def divisible(dividend,divisor):
    """Takes the first number and checks whether it is a multiple of the second (or takes a number/
    and checks whether it is a factor of the first)"""
    if dividend == 0 and divisor == 0:
        return True
    elif divisor == 0:
        return False
    elif dividend % divisor == 0:
        return True
    else:
        return False
        
        
# Number 6
def prime(number):
    """Takes a number and determines whether it is prime or not"""
    if number == 2:
        return True
    else:
        for value in range(2,int(number**.5 + 1)):
            if number % value != 0:
                return True
            else:
                return False
    

# Number 7
def isPerfect(number):
    """Checks whether a number is perfect, meaning that the sum of its factors excluding itself equals itself"""
    valuesLessThan = range(1,number)
    sumSoFar = 0
    for value in valuesLessThan:
        if number % value == 0:
            sumSoFar += value
    if sumSoFar == number:
        return True
    else:
        return False


# Number 8
def digitDivision(number):
    """Checks if the sum of the digits of a number divides evenly into the number itself"""
    sumOfDigits = sum_digits(number)
    if number % sumOfDigits == 0:
        return True
    else:
        return False
