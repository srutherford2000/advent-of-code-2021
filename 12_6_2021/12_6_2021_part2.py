#file_name='test_part1.txt'
file_name='input_part1.txt'

in_file=open(file_name)

fish = []

for i, line in enumerate(in_file):
    the_line = line.strip()
    #splite on the arrows
    nums = the_line.split(",")
    for num in nums:
        fish.append( int(float(num)) )
    

    
in_file.close()

cycle_0 = 0
cycle_1 = 0
cycle_2 = 0
cycle_3 = 0
cycle_4 = 0
cycle_5 = 0
cycle_6 = 0
cycle_7 = 0
cycle_8 = 0
for i in fish:
    if i == 0:
        cycle_0 += 1
    elif i == 1:
        cycle_1 += 1
    elif i == 0:
        cycle_0 += 1
    elif i == 2:
        cycle_2 += 1
    elif i == 3:
        cycle_3 += 1
    elif i == 4:
        cycle_4 += 1
    elif i == 5:
        cycle_5 += 1
    elif i == 6:
        cycle_6 += 1
    elif i == 7:
        cycle_7 += 1
    elif i == 8:
        cycle_8 += 1

days = 256
for day in range(days):
    hold = cycle_7
    cycle_7 = cycle_8
    if day % 7 == 0:
        cycle_8 = cycle_0
        cycle_0 += hold
    elif day% 7 == 1:
        cycle_8 = cycle_1
        cycle_1 += hold
    elif day% 7 == 2:
        cycle_8 = cycle_2
        cycle_2 += hold
    elif day% 7 == 3:
        cycle_8 = cycle_3
        cycle_3 += hold
    elif day% 7 == 4:
        cycle_8 = cycle_4
        cycle_4 += hold
    elif day% 7 == 5:
        cycle_8 = cycle_5
        cycle_5 += hold
    elif day% 7 == 6:
        cycle_8 = cycle_6
        cycle_6 += hold

total_fish = cycle_0 + cycle_1 + cycle_2 + cycle_3 + cycle_4 + cycle_5 + cycle_6 + cycle_7 + cycle_8     


print(total_fish)

