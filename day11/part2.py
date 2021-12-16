with open('data.txt', 'r') as f:
    data = f.readlines()
from pprint import pprint
data = [list(i.strip()) for i in data]
data = [[int(i) for i in j] for j in data]

pprint(data)

n_steps = 1000
flash_count = 0
flashed = list()

def flash(i, j, data):
    global flashed
    if (i,j) in flashed:
        return
    else:
        flashed.append((i,j))
        global flash_count
        flash_count += 1

    delta_neighbors = [(-1,-1), (1,1), (1,-1), (-1,1), (0,1), (1,0), (0,-1), (-1,0)] 
    for d in delta_neighbors:
        ni, nj = i+d[0], j+d[1]
        if (ni<0 or ni >= len(data)):
            continue
        if (nj<0 or nj >= len(data[0])):
            continue

        if (ni,nj) not in flashed:
            data[ni][nj] += 1
            if data[ni][nj] > 9:
                data[ni][nj] = 0
                flash(ni, nj, data)


for s in range(n_steps):
    flashed = list()
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j] += 1
            
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] > 9:
                data[i][j] = 0
                flash(i,j,data)

    print('\n')
    pprint(data)
    if len(flashed) == 100:
        print('step {0}'.format(s))
        break

print(flash_count)
