#!usr/bin/env python3

# the prime factors of 13195 are 5, 7, 13 and 29.
# what is the largest prime factor of the number 600851475143?

numMain = 600851475143
divisor = 2

while numMain > 1:
    if numMain % divisor == 0:
        print(divisor)
        numMain /= divisor
    else:
        divisor += 1

print("Largest prime factor: {}".format(divisor))
