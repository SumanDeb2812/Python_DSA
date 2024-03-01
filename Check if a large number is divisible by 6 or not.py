# Given a number, the task is to check if a number is divisible by 6 or not. The input 
# number may be large and it may not be possible to store even if we use long long int.
def divisible(main, divider):
    m = int(main)
    d = int(divider)
    if (m % d) != 0:
        print("No")
    else:
        print("Yes")

divisible(32131534531534521531,7)
