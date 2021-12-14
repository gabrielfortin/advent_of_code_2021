with open("data.txt", "r") as f:
    data = f.readlines()
data = [i.strip('\n') for i in data]


sChars = ['[', '{', '<', '(']
eChars = [']', '}', '>', ')']

def correspondingChar(char):
    try:
        index = sChars.index(char)
        return eChars[index]
    except ValueError:
        pass

    index = eChars.index(char)
    return sChars[index]

nonIllegalLines = list()
illegalCharsFound = list()
for line in data:
    print(line)
    left = list()
    right = list()
    openedAndNotClosed = list()
    corrupted = False
    for char in line:
        if char in sChars:
            left.append(char)
            openedAndNotClosed.append(char)
        if char in eChars:
            if char != correspondingChar(openedAndNotClosed[-1]):
                print("type 3 at {0}".format(char))
                corrupted = True
                illegalCharsFound.append(char)
                break
            else:
                openedAndNotClosed.pop()
                right.append(char)
    if corrupted:
        continue

    nonIllegalLines.append(line)

autoCompletedLines = list()
for line in nonIllegalLines:
    openedAndNotClosed = list()
    for i in range(len(line)):
        char = line[i]
        if char in sChars:
            openedAndNotClosed.append(char)
        elif char in eChars:
            if char == correspondingChar(openedAndNotClosed[-1]):
                openedAndNotClosed.pop()
    openedAndNotClosed.reverse()
    autoComp = ""
    for char in openedAndNotClosed:
        autoComp += correspondingChar(char)
    autoCompletedLines.append(autoComp)
    print(autoComp)

autoCompScores = list()
for line in autoCompletedLines:
    score = 0
    for char in line:
        score *= 5
        if char == ")":
            score += 1
        elif char == "]":
            score += 2
        elif char == "}":
            score += 3
        else:
            score += 4
    autoCompScores.append(score)
autoCompScores.sort()
print(autoCompScores)
print(autoCompScores[int(len(autoCompScores)/2)])

