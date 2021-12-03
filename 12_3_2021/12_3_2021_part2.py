#file_name='test_part1.txt'
file_name='input_part1.txt'

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(line.strip())

in_file.close()


def find_oxygen_generator_rating(working_list, position):
    if len(working_list) == 1:
        return working_list
    else:
        list_with_1s = []
        list_with_0s = []
        
        for binary_string in working_list:
            if binary_string[position] == "1":
                list_with_1s.append(binary_string)
            else:
                list_with_0s.append(binary_string)

        if len(list_with_1s)>=len(list_with_0s):
            return find_oxygen_generator_rating(list_with_1s, position+1)
        else:
            return find_oxygen_generator_rating(list_with_0s, position+1)


def find_co2_scrubber_rating(working_list, position):
    if len(working_list) == 1:
        return working_list
    else:
        list_with_1s = []
        list_with_0s = []
        
        for binary_string in working_list:
            if binary_string[position] == "1":
                list_with_1s.append(binary_string)
            else:
                list_with_0s.append(binary_string)

        if len(list_with_0s)<=len(list_with_1s):
            return find_co2_scrubber_rating(list_with_0s, position+1)
        else:
            return find_co2_scrubber_rating(list_with_1s, position+1)




oxygen_generator_rating = find_oxygen_generator_rating(lines,0)[0]
print("Oxygen Rating:", oxygen_generator_rating)

co2_scrubber_rating = find_co2_scrubber_rating(lines,0)[0]
print("Carbon Rating:", co2_scrubber_rating)

oxygen_generator_rating_int = int(oxygen_generator_rating,2)
co2_scrubber_rating_int = int(co2_scrubber_rating,2)

life_support_rating = oxygen_generator_rating_int*co2_scrubber_rating_int
print("Life Support Rating:",life_support_rating)
