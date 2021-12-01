#file_name='test_part1.txt'
file_name='input_part1.txt'

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(int(float(line.strip())))

in_file.close()

num_greater=0

for i in range(3,len(lines)):
    current_num = lines[i]
    last_num = lines[i-1]
    last_last_num = lines[i-2]
    last_last_last_num = lines[i-3]

    newest_3_sum = current_num + last_num + last_last_num
    last_3_sum = last_num + last_last_num + last_last_last_num  
    
    if (newest_3_sum>last_3_sum):

        num_greater += 1


print("the number of times a depth measurement increases:", num_greater)
