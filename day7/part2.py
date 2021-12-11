import math
with open("data.txt", "r") as f:
	data = f.read()

data = [int(i) for i in data.split(',')]


#data = [16,1,2,0,4,2,7,1,2,14]
data.sort()
mean = data[int(len(data)/2)]
moy = math.floor(sum(data)/len(data))
mean = moy
diffs = list()
for entry in data:
    diffs.append(abs(entry-mean))

def fn(item):
    value = 0
    count = 0
    for i in range(item):
        count += 1
        value += count
    return value

answer = sum([fn(i) for i in diffs])
print(answer)
