from random import *

color = ["red", "blue", "yellow", "green", "orange"]

total = []
loc = []

def search(i, total):
    if i < 7:
        return total[i+7:] + total[:i+7]
    elif i > 7:
        return  total[i-7:] + total[:i-7]
    elif i == 7:
        return  total         

for i in range(0, 3):
    temp = color
    shuffle(temp)
    total = total + temp

print(total)

start = color[randint(0,4)]
print("start: %s" % start)

for j in range(0, len(total)):
    if total[j] == start:
        loc.append(j)

print("Index with start color : %s" % loc)

test = start
while test == start:
    test = color[randint(0, 4)]

print("test value is: %s" % test)

work = [0,0,0]

for i in range(0, 3):
    work[i] = search(loc[i], total)

print(work)