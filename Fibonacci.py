# # using loop concept
# x = 0
# y = 1
# z = 0
# print(x, end=",")
# print(y, end=",")
# for z in range(10):
#     z = x + y
#     x = y
#     y = z
#     print(z, end=",")
# print()

# # using recursion
# # recursion is when a function calls itself
# print(0, end=",")
# print(1, end=",")
# count = 2
# def printFibo(a, b):
#     global count
#     if count <= 11:
#         c = a + b
#         a = b
#         b = c
#         print(c, end=",")
#         count += 1
#         printFibo(a, b)  # it is called recursion
#     else:
#         return
# printFibo(0, 1)

def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)

print(F(2))