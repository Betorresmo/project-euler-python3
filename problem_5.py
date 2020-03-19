#!usr/bin/env python3

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any reminder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def testDivisibility(number):

    i = 19
    while i > 10:
        if number % i != 0:
            return 0
        i -= 1

    return 1


smallestNumber = 20
while not testDivisibility(smallestNumber):
    smallestNumber += 20

print(f'The smallest number is {smallestNumber}')