with open("data.txt", 'r') as f:
    data = f.readlines()
data = [list(line.strip('\n')) for line in data]
from pprint import pprint

risklevels = list()
for i in range(len(data)):
    for j in range(len(data[i])):
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
            risklevels.append(int(item)+1)

print(sum(risklevels))


