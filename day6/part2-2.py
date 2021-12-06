from datetime import datetime
date_start = datetime.now()

days = 256


with open("data.txt", 'r') as f:
	data = f.read()
fishes_init = [int(i) for i in data.split(',')]

dist = [fishes_init.count(i) for i in range(9)]

for i in range(days):
	n = dist[0]
	dist = dist[1:]
	dist[6] += n
	dist += [n]

print(sum(dist))


print(datetime.now()-date_start)

