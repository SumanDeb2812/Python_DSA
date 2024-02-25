# Given an array A[] of n numbers and another number x, the task is to check
# whether or no there exist two elements in A[] whose sum is exactly x.

#ans:
# A = [0, -1, 2, -3, 1]
# x = -2
A = [1, -2, 1, 0, 5]
x = 0
i = 0
while i < len(A):
    j = 0
    while j < len(A):
        k = A[i] + A[j]
        if k == x:
            result = "yes"
        else:
            result = "no"
        j += 1
    i += 1
print(result)
