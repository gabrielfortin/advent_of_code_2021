with open("data.txt", 'r') as f:
    lines = f.readlines()

gamma_rate = ""
epsilon_rate = ""

for i in range(0, len(lines[0])-1):
    col = [line[i] for line in lines]
    
    zero_count = col.count("0")
    one_count = col.count("1")

    if zero_count > one_count:
        gamma_rate += "0"
        epsilon_rate += "1"
    else:
        gamma_rate += "1"
        epsilon_rate += "0"
    
gamma_rate_dec = int(gamma_rate, 2)
epsilon_rate_dec = int(epsilon_rate, 2)

power_cons = gamma_rate_dec * epsilon_rate_dec
print(power_cons)