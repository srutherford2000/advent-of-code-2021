#file_name='test_part1.txt'
#file_name='test_part2.txt'
#file_name='test_part3.txt'
file_name='input_part1.txt'

in_file=open(file_name)

connections ={}

for line in in_file:
    the_line = line.strip()
    #splite on the -
    [cave1,cave2] = the_line.split("-")

    if cave1 in connections:
        connections[cave1] = connections[cave1] +[cave2]
    else:
        connections[cave1] = [cave2]

    
    if cave2 in connections:
        connections[cave2] = connections[cave2] +[cave1]
    else:
        connections[cave2] = [cave1]
    

    
in_file.close()


paths_to_check = [['start',[]]]
paths_finished = []

while paths_to_check != []:
    #print(paths_to_check)
    item = paths_to_check[0][0]
    old_path = paths_to_check[0][1]
    paths_to_check = paths_to_check[1:]

    possible_new_paths = connections[item]
    for path in possible_new_paths:
        if path.islower() and (path in old_path):
            pass
        elif path == 'end':
            new_path = old_path + [item] + [path]
            paths_finished.append(new_path)
        else:
            new_path = old_path + [item]
            if new_path not in paths_to_check :
                paths_to_check.append([path, new_path])

print(len(paths_finished))


    
