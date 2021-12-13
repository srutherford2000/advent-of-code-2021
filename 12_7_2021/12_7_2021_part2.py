#file_name='test_part1.txt'
file_name='input_part1.txt'

in_file=open(file_name)

nums_as_strs = []

for line in in_file:
    the_line = line.strip()
    nums_as_strs = the_line.split(",")
    

    
in_file.close()

min_num =  10000000000
max_num = -10000000000

nums = []
for str_num in nums_as_strs:
    int_num = int(float(str_num))
    nums.append(int_num)
    if int_num > max_num:
        max_num = int_num
    if int_num < min_num:
        min_num = int_num

best = 10000000000
distance_to_fuel_map = {}

def find_sum_of_step(num):
    the_val = 0
    for i in range(1,num+1):
        the_val += i
    return the_val


for num in range(min_num, max_num+1):
    total_movment = 0
    for num2 in nums:
        distance = abs(num-num2)
        if distance in distance_to_fuel_map:
            fuel = distance_to_fuel_map[distance]
        else:
            fuel = find_sum_of_step(distance)
            distance_to_fuel_map[distance] = fuel
        total_movment += fuel
    if total_movment < best:
        best = total_movment

print(best)
