#orignal code from https://www.tutorialgateway.org/python-program-to-find-factors-of-a-number/
import os

# os.system ("say hello")

number = int(input("Please Enter any Number: "))

value = 1
print("Factors of a Given Number {0} are:".format(number))
os.system ("say I am Factor-tron - the factors are")
while (value <= number):
    if(number % value == 0):
        print("{0}".format(value))
        z = "say " + str(value)
        os.system (z)
    value = value + 1
