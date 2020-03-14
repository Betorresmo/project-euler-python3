# Find the sum of all the multiples of 3 or 5 below 1000

numCounter = 0

for i in range(0, 1000):
    if i % 5 == 0 or i % 3 == 0:
        numCounter = numCounter + i
        print(numCounter)
print("Sum: {}".format(numCounter))
