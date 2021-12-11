#file_name='test_part1.txt'
file_name='input_part1.txt'

in_file=open(file_name)

coordinates = []
max_dimension = 0

for i, line in enumerate(in_file):
    the_line = line.strip()
    #splite on the arrows
    [part1,part2] = the_line.split(" -> ")
    new_part1 = part1.split(",")
    new_part2 = part2.split(",")

    part1_int = []
    for num in new_part1:
        inty = int(float(num))
        part1_int.append(inty)
        if inty>max_dimension:
            max_dimension = inty


    part2_int = []
    for num in new_part2:
        inty = int(float(num))
        part2_int.append(inty)
        if inty>max_dimension:
            max_dimension = inty

    coor = [part1_int , part2_int]
    coordinates.append(coor)
    

    
in_file.close()

ocean_floor = []
for i in range(max_dimension +1):
    row = []
    for j in range(max_dimension+1):
        row.append(0)
    ocean_floor.append(row)

for coor in coordinates:
    x0 = coor[0][0]
    y0 = coor[0][1]
    x1 = coor[1][0]
    y1 = coor[1][1]

    #vertical line
    if x0==x1 and y0!=y1:
        if y0>y1:
            for i in range(y1,y0+1):
                ocean_floor[i][x0] += 1
        else:
            for i in range(y0,y1+1):
                ocean_floor[i][x0] += 1
            
    elif y0==y1 and x0!=x1:
        if x0>x1:
            for i in range(x1,x0+1):
                ocean_floor[y0][i] += 1
        else:
            for i in range(x0,x1+1):
                ocean_floor[y0][i] += 1

    elif x0-x1>0:
        if y0-y1>0:
            j = y1
            for i in range(x1, x0+1):
                ocean_floor[j][i] += 1
                j += 1
        else:
            j = y1
            for i in range(x1, x0+1):
                ocean_floor[j][i] += 1
                j -= 1
    elif x0-x1<0:
        if y0-y1>0:
            j = y0
            for i in range(x0, x1+1):
                ocean_floor[j][i] += 1
                j -= 1
        else:
            j = y0
            for i in range(x0, x1+1):
                ocean_floor[j][i] += 1
                j += 1
    else:
        print("bad")
            
            

num_bigger_than_1 = 0


for i in range(max_dimension +1):
    for j in range(max_dimension+1):
        if ocean_floor[i][j] > 1:
            num_bigger_than_1 += 1

print("Overlaps:", num_bigger_than_1)
                

