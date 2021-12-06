with open("data.txt", 'r') as f:
    lines = f.readlines()

def process(lines, most_common, as_decimal=False):
    lines_list = lines
    for i in range(0, len(lines_list[0])-1):
        col = [line[i] for line in lines_list]
        
        zero_count = col.count("0")
        one_count = col.count("1")

        if (zero_count > one_count and most_common) or (zero_count <= one_count and not most_common):
            lines_list = [line for line in lines_list if line[i] == "0"]
        elif (zero_count <= one_count and most_common) or (zero_count > one_count and not most_common):
            lines_list = [line for line in lines_list if line[i] == "1"]
  
        if len(lines_list) == 1:
            break
    
    number = lines_list[0].strip('\n')
    return number if not as_decimal else int(number, 2)

o2 = process(lines, True, True)
co2 = process(lines, False, True)

print(o2 * co2)