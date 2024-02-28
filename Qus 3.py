# Given an array, the task is to find average of that array. Average is the sum of array 
# elements divided by the number of elements.

#Iterative
def findAvg(array):
    sum = array[0]
    for i in range(1, len(array)):
        sum = sum + array[i]
    print(int(sum / len(array)));

#Recursion
count = 0
a = 0
def findAvgRe(array):
    b = 1
    global a
    global count
    if count < len(array):
        a = a + array[count]
        count += 1
        findAvgRe(array)
    else:
        return
    return int(a / len(array))

print(findAvgRe([1,2,3]))