with open("input.txt", "r") as f:
    data_lines = f.readlines()

numbers = [int(i) for i in data_lines]

sums = [sum(numbers[index:index+3]) for index in range(0, len(numbers)-2)]

increased = len([sums[i] for i in range(1, len(sums)) if sums[i] > sums[i-1]])

print(increased)