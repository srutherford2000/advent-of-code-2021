#file_name='test_part1.txt'
file_name='input_part1.txt'

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(line.strip())

in_file.close()

count_ones_per_space = {}

for binary_code in lines:
    for i,digit in enumerate(binary_code):
        if digit == "1":
            if i in count_ones_per_space.keys():
                count_ones_per_space[i] += 1
            else:
                count_ones_per_space[i] = 1

gamma_rate = ""
epsilon_rate = ""

half = len(lines)/2

for the_key in range(len(count_ones_per_space)):
    the_val = count_ones_per_space[the_key]
    if the_val > half:
        gamma_rate = gamma_rate +"1"
        epsilon_rate = epsilon_rate +"0"
    else:
        gamma_rate = gamma_rate +"0"
        epsilon_rate = epsilon_rate +"1"
        

print("Gamma Rate:",gamma_rate)
print("Epsilon Rate:",epsilon_rate)

gamma_rate_as_int = int(gamma_rate,2)
epsilon_rate_as_int = int(epsilon_rate,2)
power_consumption = gamma_rate_as_int*epsilon_rate_as_int

print("Power Consumption:", power_consumption)
