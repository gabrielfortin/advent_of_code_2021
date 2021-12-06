with open("input.txt", "r") as f:
    data_lines = f.readlines()

numbers = [int(i) for i in data_lines]

increased_list = len([numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i-1]])

print(increased_list)
