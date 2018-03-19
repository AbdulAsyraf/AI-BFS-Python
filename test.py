from random import *

color = [1, 2, 3, 4, 5]

total = []
loc = []

for i in range(0, 3):
    temp = color
    shuffle(temp)
    total = total + temp

print(total)

start = randint(1,5)
print("start: %i" % start)

for j in range(0, len(total)):
    if total[j] == start:
        print(j)
        loc.append(j)

print(loc)

test = start
while test == start:
    test = randint(1, 5)
    print("=")

print("test: %i" % test)