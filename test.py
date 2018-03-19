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
        for j in range(0, 3):
            temp1 = state[j][7-i]
            temp2 = state[j][7+i]
            if temp1 == target:
                answer.append(j)
                answer.append(-i)
                break
            elif temp2 == target:
                answer.append(j)
                answer.append(i)
                break
        if len(answer) != 0:
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

for i in range(0, 3):
    temp = color
    shuffle(temp)
    total = total + temp

print(total)

start = test
while start == test:
    start = color[randint(0, 4)]

print("Randomly chosen starting color: %s" % start)

for j in range(0, len(total)):
    if total[j] == start:
        loc.append(j)

print("Indices with starting color: %s" % loc)

work = [0,0,0]

for i in range(0, 3):
    work[i] = setup(loc[i], total)

answer = []
search(work, test, answer)

if answer[1] < 0:
    part2 = " %i step(s) to the left"
else:
    part2 = " %i step(s) to the right"

part1 = "The color %s is found after searching from index %i"
whole = part1 + part2

answer[1] = abs(answer[1])
print(whole % (test, loc[answer[0]], answer[1]))