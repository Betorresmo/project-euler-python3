#!usr/bin/env python3

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum


def sumOfTheSquares(nthNumber):

    sumSquares = 0
    for i in range(1, nthNumber+1):
        sumSquares += pow(i, 2)

    return sumSquares


def squareOfTheSum(nthNumber):

    sqrSum = 0
    for i in range(1, nthNumber+1):
        sqrSum += i

    return pow(sqrSum, 2)


print(f'The difference is {squareOfTheSum(100) - sumOfTheSquares(100)}')

