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


days  = 80
                
for day in range(days):
    new_fish = []
    for i,f in enumerate(fish):
        if f == 0:
            new_fish.append(8)
            fish[i] = 6
        else:
            fish[i] = fish[i] -  1
    if new_fish != []:
        fish+= new_fish
        
print("Num fish after 80 days:", len(fish))
