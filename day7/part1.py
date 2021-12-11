with open("data.txt", "r") as f:
	data = f.read()

data = [int(i) for i in data.split(',')]
data.sort()
mean = data[int(len(data)/2)]

diffs = list()
for entry in data:
    diffs.append(abs(entry-mean))

print(sum(diffs))
