from random import *

def setup(i, total):
    if i < 7:
        return total[i+8:] + total[:i+7]
    elif i > 7:
        return  total[i-7:] + total[:i-7]
    elif i == 7:
        return  total         

def search(state, target, answer):
    for i in range(1, 7):
        temp1 = state[7-i]
        temp2 = state[7+i]
        if temp1 == target:
            answer.append(-i)
            break
        elif temp2 == target:
            answer.append(i)
            break

color = ["Red", "Blue", "Yellow", "Green", "Orange"]

total = []
loc = []

print("0 - RED")
print("1 - BLUE")
print("2 - YELLOW")
print("3 - GREEN")
print("4 - ORANGE")
check = input("Please enter a number to search for the color: ")

test = color[check]

print("The color %s is chosen" % test)

for i in range(0, 3):
    temp = color
    shuffle(temp)
    total = total + temp

print(total)

start = test
while start == test:
    start = color[randint(0, 4)]

for j in range(0, len(total)):
    if total[j] == start:
        loc.append(j)

startLoc = loc[randint(0, 2)]

print("Initial position of the funnel is underneath the color %s at index %i" % (start, startLoc))

work = setup(startLoc, total)

answer = []
search(work, test, answer)

if answer[0] < 0:
    part2 = " %i step(s) to the left"
else:
    part2 = " %i step(s) to the right"

part1 = "The color %s is found after searching"
whole = part1 + part2

answer[0] = abs(answer[0])
print(whole % (test, answer[0]))