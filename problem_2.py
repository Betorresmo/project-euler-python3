#!usr/bin/env python3

# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

firstTerm = 1
secondTerm = 2
termSum = 0
evenNumSum = 0
while evenNumSum < 4000000:
    termSum = firstTerm + secondTerm
    firstTerm = secondTerm
    secondTerm = termSum
    if secondTerm % 2 == 0:
        evenNumSum = evenNumSum + secondTerm
print(evenNumSum)