from pprint import pprint
with open("data.txt", "r") as f:
    data = f.readlines()

pprint(data)

outputs = list()
for line in data:
    alist = line.split('|')[1]
    alist = alist.strip('\n')
    if alist[0] == ' ':
        alist = alist[1:]
    outputs += alist.split(' ')

pprint(outputs)

count = 0
for output in outputs:
    if len(output) == 2 or len(output) ==3 or len(output) == 4 or len(output) == 7:
        count += 1
print(count)
