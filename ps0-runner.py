# Import file containing all functions
import ps0

program = raw_input("Which program would you like to run?\n0. Odd or even\n1. Number of Digits\n2. Sum of Digits\n3. Sum of integers\n\
4. Factorial\n5. Divisibility\n6. Prime\n7. Perfect\n8. Digits Factor of Number\n")


# Number 0
if program == "0":
    print("Case 1: Try odd number")
    print("Is 7 an even number? {}".format(ps0.is_even(7)))
    print("Case 2: Try an even number")
    print("Is 10 an even number? {}".format(ps0.is_even(10)))
    print("Case 3: Try 0 (even though it is an even integer)")
    print("Is 0 an even number? {}".format(ps0.is_even(10)))


# Number 1
elif program == "1":
    print("Case 1: Try a number with 1 digit")
    print("How many digits does 6 have? {}".format(ps0.length(6)))
    print("Case 2: Try a number with 3 digits")
    print("How many digits does 121 have? {}".format(ps0.length(121)))
    print("Case 3: Try a number with 7 digits")
    print("How many digits does 3847502 have? {}".format(ps0.length(3847502)))
    print("Case 4: Try 0")
    print("How many digits does 0 have? {}".format(ps0.length(0)))


# Number 2
elif program == "2":
    print("Case 1: Try a random number")
    print("What is the sum of the digits of 271? {}".format(ps0.sum_digits(271)))
    print("Case 2: Try another random number")
    print("What is the sum of the digits of 2987? {}".format(ps0.sum_digits(2987)))
    print("Case 3: Try 0")
    print("What is the sum of the digits of 0? {}".format(ps0.sum_digits(0)))


# Number 3
elif program == "3":
    print("Case 1: Try a random number")
    print("What is the sum of all the integers from 0 to 8 excluding 8? {}".format(ps0.sum_ints(8)))
    print("Case 2: Try a random number")
    print("What is the sum of all the integers from 0 to 5 excluding 5? {}".format(ps0.sum_ints(5)))
    print("Case 3: Try 0")
    print("What is the sum of all the integers from 0 to 0? {}".format(ps0.sum_ints(0)))

# Number 4
elif program == "4":
    print("Case 1: Try a random number")
    print("What is 4! ? {}".format(ps0.factorial(4)))
    print("Case 2: Try a random number")
    print("What is 8! ? {}".format(ps0.factorial(8)))
    print("Case 3: Try 0")
    print("What is 0! ? {}".format(ps0.factorial(0)))

# Number 5
elif program == "5":
    print("Case 1: Try a number that divides evenly into the other")
    print("Is 3 a factor of 6? {}".format(ps0.divisible(6,3)))
    print("Case 2: Try a number that does not divide evenly into the other")
    print("Is 4 a factor of 21? {}".format(ps0.divisible(21,4)))
    print("Case 3: Try a scenario where 0 is the divisor")
    print("Is 0 a factor of 12? {}".format(ps0.divisible(12,0)))
    print("Case 4: Try a scenario where 0 is the dividend and divisor")
    print("Is 0 a factor of 0? {}".format(ps0.divisible(0,0)))

# Number 6
elif program == "6":
    print("Case 1: Try a non-prime number")
    print("Is 8 a prime number? {}".format(ps0.prime(8)))
    print("Case 2: Try a prime number")
    print("Is 19 a prime number? {}".format(ps0.prime(19)))


# Number 7
elif program == "7":
    print("Case 1: Try a perfect number")
    print("Is 6 a perfect number? {}".format(ps0.isPerfect(6)))
    print("Case 2: Try a non-perfect number")
    print("Is 8 a perfect number? {}".format(ps0.isPerfect(8)))

# Number 8
elif program == "8":
    print("Case 1: Try a number in which the sum of the digits divide evenly into the number")
    print("Do the sum of the digits of 120 divide evenly into 120? {}".format(ps0.digitDivision(120)))
    print("Case 2: Try a number in which the sum of the digits do not divide evenly into the number")
    print("Do the sum of the digits of 154 divide evenly into 154? {}".format(ps0.digitDivision(154)))








