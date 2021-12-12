from pprint import pprint
with open("data.txt", "r") as f:
    data = f.readlines()


odata  = list()

for line in data:
    entry = dict()
    line = line.strip('\n')
    entry['L'] = line.split('|')[0].split(' ')
    if entry['L'][-1] == '':
        entry['L'].pop()
    
    entry['output'] = line.split('|')[1]
    if entry['output'][0] == ' ':
        entry['output'] = entry['output'][1:]

    entry['output'] = entry['output'].split(' ')
    odata.append(entry)

def listsCoincide(lista, listb):
    if len(lista) != len(listb):
        return False
    for ia in lista:
        if ia not in listb:
            return False
    return True

def listsCoincide2(listsa, listb):
    for lista in listsa:
        a = listsCoincide(lista, listb)
        if a is True:
            return True
        
    return False


def listIncludesList(lista, listb):
    for item in listb:
        if item not in lista:
            return False
    return True

def diffLists(biggerList, smallerList):
    diff = list()
    for item in biggerList:
        if item not in smallerList:
            diff.append(item)
    return diff

def sortedStr(string):
    asList = list(string)
    asList.sort()
    return "".join(asList)

for entry in odata:
    zero = None
    one = None
    two = None
    three = None
    four = None
    five = None
    six = None
    seven = None
    eight = None
    nine = None

    n = [[], [], [], [], [], [], [], [], [], []] 
    L = entry['L'] + entry['output']
    rightseg = None
    topseg = None
    diff78 = None
    diff14 = None
    for item in L:
        if len(item) == 2:
            one = item
            if sortedStr(item) not in n[1]:
                n[1].append(sortedStr(item))
        if len(item) == 7:

            eight = item
            if sortedStr(item) not in n[8]:
                n[8].append(sortedStr(item))
        if len(item) == 4:
            four = item
            if sortedStr(item) not in n[4]:
                n[4].append(sortedStr(item))
        if len(item) == 3:
            seven = item
            if sortedStr(item) not in n[7]:
                n[7].append(sortedStr(item))
    L = entry['L'] + entry['output']
    for item in L:
        found = False
        if len(item) == 5:
            if one is not None:
                if one[0] in item and one[1] in item:
                    three = item
                    if sortedStr(item) not in n[3]:
                        n[3].append(sortedStr(three))
                    continue
                if four is not None:
                    if sum([letter in item for letter in four]) == 3:
                        if sortedStr(item) not in n[5]:
                            n[5].append(sortedStr(item))
                        continue
                    else:
                        if sortedStr(item) not in n[2]:
                            n[2].append(sortedStr(item))
                        continue

        if len(item) == 6:
            if one is not None:
                if (one[0] not in item or one[1] not in item):
                    six = item
                    if sortedStr(six) not in n[6]:
                        n[6].append(sortedStr(six))
                    continue
                
            if four is not None:
                if listIncludesList(item, four):
                    nine = item
                    if sortedStr(nine) not in n[9]:
                        n[9].append(sortedStr(item))
                    continue
                else:
                    if sortedStr(item) not in n[0]:
                        n[0].append(sortedStr(item))
                    zero = item
                    continue
        
    
    number = ""
   # n = [zero, one, two, three, four, five, six , seven , eight, nine]
    for item in entry['output']:
        
        if listsCoincide2(n[0], item):
            number += str(0) 
        elif listsCoincide2(n[1], item):
            number += str(1)
        elif listsCoincide2(n[2], item):
            number += str(2)
        elif listsCoincide2(n[3], item):
            number += str(3)
        elif listsCoincide2(n[4], item):
            number += str(4)
        elif listsCoincide2(n[5], item):
            number += str(5)
        elif listsCoincide2(n[6], item):
            number += str(6)
        elif listsCoincide2(n[7], item):
            number += str(7)
        elif listsCoincide2(n[8], item):
            number += str(8)
        elif listsCoincide2(n[9], item):
            number += str(9)
        else:
            number += 'x'

    entry["result"] = number
        

print(sum([int(entry["result"]) for entry in odata]))
