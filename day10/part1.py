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
            #if correspondingChar(char) not in left:
            #    print("error at {0}".format(char))
            #    corrupted = True
            #    break
            #openerCount = left.count(correspondingChar(char))
            #closerCount = right.count(char)

            #if openerCount == closerCount:
            #    print("type 2 error at {0}".format(char))
            #    corrupted = True
            #    break

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


score = 0
for illegal in illegalCharsFound:
    if illegal == ")":
        score += 3
    elif illegal == "]":
        score += 57
    elif illegal == "}":
        score += 1197
    else:
        score += 25137

print(score)
