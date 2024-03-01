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

dist = {'1':'suman', '2':'ram', '3':'sham', '4':'jadhu', '5':'madhu'}
for key in "12345":
    print(dist[key], end=", ")