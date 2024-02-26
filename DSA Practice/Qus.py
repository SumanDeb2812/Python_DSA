# For the given array of integers, count even and odd elements.

def findEvenOdd(array):
    countEven = 0
    countOdd = 0
    for i in range(0, len(array)):
        if array[i] & 1 == 1:
            countOdd += 1
        else:
            countEven += 1
    print("Count of even number:", countEven)
    print("Count of odd number:", countOdd)

findEvenOdd([1, 5, 9, 12])
