#file_name='test_part1.txt'
file_name='input_part1.txt'

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(line.strip())

in_file.close()

position = 0
depth = 0

for line in lines:
    [direction, num] = line.split(" ")
    num = int(float(num))
    if direction == "forward":
        position += num
    elif direction == "up":
        depth -= num
    elif direction == "down":
        depth += num

product = position*depth
print("pos:", position, "depth:",depth, "product:", product)
