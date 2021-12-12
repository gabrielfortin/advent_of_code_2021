from pprint import pprint
with open("data.txt", "r") as f:
    data = f.readlines()

print(data)

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
pprint(odata)

def listsCoincide(lista, listb):
    if len(lista) != len(listb):
        return False
    for ia in lista:
        if ia not in listb:
            return False
    return True

def listIncludesList(lista, listb):
    for item in listb:
        if item not in lista:
            return False
    return True

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

    rightseg = None
    topseg = None
    diff78 = None
    diff14 = None
    for item in entry['L']:
        if len(item) == 2:
            one = item
        if len(item) == 7:
            eight = item
        if len(item) == 4:
            four = item
        if len(item) == 3:
            seven = item
        
        if one is not None and rightseg is None:
            rightseg = one

        if one is not None and seven is not None and topseg is None:
            topseg = None
            for item in seven:
                if item not in one:
                    topseg = item
        
        if seven is not None and eight is not None and diff78 is None:
            diff78 = list()
            for item in eight:
                if item not in seven:
                    diff78.append(item)

        
        if one is not None and four is not None and diff14 is None:
            diff14 = list()
            for item in four:
                if item not in one:
                    diff14.append(item)
        
        if rightseg is not None and four is not None and seven is not None and eight is not None and not listsCoincide(item, rightseg) and listIncludesList(item, rightseg) and not listsCoincide(item, four) and not listsCoincide(item, seven) and not listsCoincide(item, eight):
            if len(item) == 5:
                three = item    

            elif len(item) == 6:
                print("03")

        if diff78 is not None and topseg is not None and listIncludesList(item, topseg) and listIncludesList(item, diff78):
            six = item

        #if eight is not None and rightseg is not None:

        if diff78 is not None and topseg is not None:
            three = diff78 + [topseg]

        if len(item) == 6:
            if rightseg is not None:
                if rightseg[0] in item and rightseg[1] in item:
                    if diff14 is not None:
                        if diff14[0] in item and diff14[1] in item:
                            nine = item
                        else:
                            zero = item

                else:
                    if six is None:
                        six = item

        if len(item) == 5:
            found = False
            if rightseg is not None:
                if rightseg[0] in item and rightseg[1] in item:
                    three = item
                    found = True
            if not found:
                if diff14 is not None:
                    if diff14[0] not in item or diff14[1] not in item:
                        two = item
                    else:
                        five = item

    
    print('---')
    for item in entry['output']:
        if zero is not None and listsCoincide(zero, item):
            print(0)
        if one is not None and listsCoincide(one, item):
            print(1)
        if two is not None and listsCoincide(two, item):
            print(2)
        if three is not None and listsCoincide(three, item):
            print(3)
        if four is not None and listsCoincide(four, item):
            print(4)
        if five is not None and listsCoincide(five, item):
            print(5)
        if six is not None and listsCoincide(six, item):
            print(6)
        if seven is not None and listsCoincide(seven, item):
            print(7)
        if eight is not None and listsCoincide(eight, item):
            print(8)
        if nine is not None and listsCoincide(nine, item):
            print(9)




