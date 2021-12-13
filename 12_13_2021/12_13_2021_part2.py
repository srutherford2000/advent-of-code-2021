#file_name='test_part1.txt'
file_name='input_part1.txt'

in_file=open(file_name)


lines = []
for line in in_file:
    the_line = line.strip()
    lines.append(the_line)  

    
in_file.close()

coordinates = []
folds = []

doing_folds = False
x_max_dimension = 0
y_max_dimension = 0

for l in lines:
    if l =="":
        doing_folds = True
    elif doing_folds == False:
        [num1,num2] = l.split(",")
        num1_int = int(float(num1))
        num2_int = int(float(num2))
        if(num1_int > x_max_dimension):
            x_max_dimension = num1_int
        if num2_int >y_max_dimension:
            y_max_dimension = num2_int
        coor = [num1_int,num2_int]
        coordinates.append(coor)
    elif doing_folds == True:
        [dontcare,dontcare2,goodpart] = l.split()
        [direction, num ] = goodpart.split("=")
        new_fold = [direction, int(float(num))]
        folds.append(new_fold)

paper = []
for i in range(y_max_dimension+1):
    row = ["."]*(x_max_dimension+1)
    paper.append(row)

for coor in coordinates:
    x = coor[0]
    y = coor[1]
    paper[y][x] = "#"

last_y_fold = 100000000
last_x_fold = 10000000
for fold in folds:
    direction = fold[0]
    num = fold[1]

    if direction == "y":
        for i, coor in enumerate(coordinates):
            y = coor[1]
            if y > num:
                new_y = num - (y - num)
                x = coor[0]
                paper[new_y][x] = "#"
                paper[y][x] = "."
                coordinates[i] = [x, new_y]
        last_y_fold = num
    
            
    elif direction == "x":
        for i, coor in enumerate(coordinates):
            x = coor[0]
            if x > num:
                new_x = num - (x - num)
                y = coor[1]
                paper[y][new_x] = "#"
                paper[y][x] = "."
                coordinates[i] = [new_x, y]
        last_x_fold = num
        
for row in paper[:last_y_fold+1]:
    print(row[:last_x_fold])

            
