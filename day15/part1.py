with open("datat.txt", "r") as f:
    data = f.readlines()

data = [list(line.strip()) for line in data]
from pprint import pprint

pprint(data)

currentPos = (0, 0)
endPos = (len(data)-1, len(data[0])-1)

trajet = [[currentPos[0], currentPos[1], int(data[currentPos[0]][currentPos[1]])]]
finished = False
while(not finished):
    if endPos == currentPos:
        finished = True
        break

    positions = [(currentPos[0],currentPos[1]+1), (currentPos[0]+1, currentPos[1]),
                 (currentPos[0], currentPos[1]-1), (currentPos[0]-1, currentPos[1])]
    around = [[pos[0], pos[1], int(data[pos[0]][pos[1]])] for pos in positions if pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(data) and pos[1] < len(data[0])]
    
    minimum = ['x', 'y', 10000]
    for pos in around:
        if pos[2]+sum([i[2] for i in trajet]) < minimum[2]:
            minimum = pos

    trajet.append(minimum)
    currentPos = (minimum[0], minimum[1])


print('trajet :')
print(trajet)

for i in trajet:
    data[i[0]][i[1]] = 'X'

pprint(data)
