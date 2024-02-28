# simple loop
a = 1
for a in range(1, 11):
    print(a, end=",")
    
print()
# recursion
def loop(a):
    if(a < 11):
        print(a, end=",")
        a += 1
        loop(a)
    else:
        return
loop(1)
