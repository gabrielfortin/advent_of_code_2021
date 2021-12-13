with open("data.txt", 'r') as f:
    data = f.readlines()
data = [list(line.strip('\n')) for line in data]

def checkAround(i, j, data):
    top = None
    right = None
    down = None
    left = None

    try:
    	if i-1 >= 0:
        	top = int(data[i-1][j])
    except:
        pass
    try:
        right = int(data[i][j+1])
    except:
        pass
    try:
        down = int(data[i+1][j])
    except:
        pass
    try:
        if j-1 >= 0:
            left = int(data[i][j-1])
    except:
        pass
    return [top, right, down, left]

riskLevels = list()
lowPoints = list()
for i in range(len(data)):
    for j in range(len(data[i])):
        r = checkAround(i, j, data)
       	
        top = r[0]
        right = r[1]
        down = r[2]
        left = r[3]

        item = int(data[i][j])
        
        smaller = [True, True, True, True]

        if top is not None:
            smaller[0] = item < top
        if right is not None:
            smaller[1] = item < right
        if down is not None:
            smaller[2] = item < down
        if left is not None:
            smaller[3] = item < left

        if sum(smaller) == 4:
            lowPoints.append((i,j))
            riskLevels.append(item+1)

print(sum(riskLevels))

def checkBassin(i, j, data):
    around = checkAround(i, j, data)
    
    bassin = [[int(data[i][j]),i,j]]

    top = around[0]
    right = around[1]
    down = around[2]
    left = around[3]

    if top is not None and top > int(data[i][j]) and top < 9:
        mlwd(bassin, checkBassin(i-1, j, data))
    if right is not None and right > int(data[i][j]) and right<9:
        mlwd(bassin, checkBassin(i, j+1, data))
    if down is not None and down > int(data[i][j]) and down<9:
        mlwd(bassin, checkBassin(i+1, j, data))
    if left is not None and left > int(data[i][j]) and left<9:
        mlwd(bassin, checkBassin(i, j-1, data))

    return bassin

def mlwd(lista, listb):
    for item in listb:
        if item not in lista:
            lista.append(item)

bassins = list()
for lowPoint in lowPoints:

    i = lowPoint[0]
    j = lowPoint[1]
    

    bassins.append(checkBassin(i,j,data))

bassinLengths = [len(bassin) for bassin in bassins]
print(bassinLengths)

bassinLengths.sort()

print(bassinLengths[-1]*bassinLengths[-2]*bassinLengths[-3])

    
