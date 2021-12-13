file_name='test_part1.txt'
#file_name='input_part1.txt'

in_file=open(file_name)

nums_as_strs = []

for line in in_file:
    the_line = line.strip()
    nums = the_line.split(",")
    

    
in_file.close()

nums = []
for str_num in nums_as_strs:
    nums.append(int(float(str_num)))

best = 100000000
for num in nums:
    total_movment = 0
    for num2 in nums:
        total_movment += abs(num-num2)
    if total_movment < best:
    best = total_movment

print(best)
