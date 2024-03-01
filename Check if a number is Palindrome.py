# Given a positive integer, write a function that returns true if the given number is a palindrome, else false.
def isPalindrome(number):
    n = str(number)
    i = len(n)-1
    p = ""
    while i >= 0:
        p += n[i]
        i -= 1
    if p == n:
        print("Yes")
    else:
        print("No")
isPalindrome(12321)
