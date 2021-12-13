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


paths_to_check = [['start',[],False]]
paths_finished = []



while paths_to_check != []:
    #print(paths_to_check)
    item = paths_to_check[0][0]
    old_path = paths_to_check[0][1]
    gone_to_small_cave_twice = paths_to_check[0][2]
    paths_to_check = paths_to_check[1:]

    possible_new_paths = connections[item]
    for path in possible_new_paths:
        if path == 'start':
            pass
        elif path == 'end':
            new_path = old_path + [item] + [path]
            paths_finished.append(new_path)
        elif path.islower() and (old_path.count(path) >= 2):
            pass
        elif path.islower() and (old_path.count(path) == 1) and (gone_to_small_cave_twice==True):
            pass
        elif path.islower() and (old_path.count(path) == 1) and (gone_to_small_cave_twice==False):
            new_path = old_path + [item]
            if new_path not in paths_to_check :
                paths_to_check.append([path, new_path, True])
        else:
            new_path = old_path + [item]
            if new_path not in paths_to_check :
                paths_to_check.append([path, new_path,gone_to_small_cave_twice ])

print(len(paths_finished))


    
