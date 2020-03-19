#!usr/bin/env python3

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit-numbers
# is 9009 = 91*99

# Find the largest palindrome made from the product of two 3-digit-numbers


def testIfPalindrome(num):
    numInString = str(num)
    reversedString = numInString[len(numInString)::-1]
    return reversedString == numInString if 1 else 0


class biggestPalindrome:
    firstFactor = 0
    secondFactor = 0
    value = 0


for firstFactor in range(900, 999):
    for secondFactor in range(900, 999):
        product = firstFactor * secondFactor

        if testIfPalindrome(product) and product > biggestPalindrome.value:
            biggestPalindrome.value = product
            biggestPalindrome.firstFactor = firstFactor
            biggestPalindrome.secondFactor = secondFactor

print("{} x {} = {}".format(biggestPalindrome.firstFactor, biggestPalindrome.secondFactor, biggestPalindrome.value))

            






