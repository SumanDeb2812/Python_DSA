li = ['suman', 'ram', 'sham', 'jadhu', 'madhu']

# 1st type of iteration
for x in li:
    print(x, end=", ")
print()

# 2nd type of iteration
for x in range(len(li)):
    print(li[x], end=", ")
print()

# 3rd type of iteration
i = 0
while i < len(li):
    print(li[i], end=", ")
    i += 1
print()

for x in "12345":
    print(li[x])