#file_name='test_part1.txt'
file_name='input_part1.txt'

in_file=open(file_name)

bingo_nums = []
board_list = []

cur_board=[]
j=0

for i, line in enumerate(in_file):
    the_line = line.strip()
    if i == 0:
        str_bingo_nums = the_line.split(",")
        bingo_nums = []
        for num in str_bingo_nums:
            bingo_nums.append(int(float(num)))
        
    elif i == 1:
        pass
    elif the_line == "":
        board_list.append(cur_board)
        j+=1
        cur_board = []
    else:
        new_nums = the_line.split()
        new_nums_int = []
        for num in new_nums:
            new_nums_int.append(int(float(num)))
        cur_board.append(new_nums_int)

board_list.append(cur_board)
in_file.close()


def find_winning_lists_from_board(board):
    winning_lists = []
    for row in board:
        winning_lists.append(row)
        
    for i in range(5):
        col = []
        for j in range(5):
            col.append(board[j][i])
        winning_lists.append(col)


    return winning_lists



earliest_winner = len(bingo_nums)
winning_board = []

for board in board_list:
    winning_combos = find_winning_lists_from_board(board)
    for bingo in winning_combos:
        latest_num = 0
        nums_checked = 0
        for num in bingo:
            if num not in bingo_nums:
                break
            else:
                the_ind = bingo_nums.index(num)
                nums_checked += 1
                if (the_ind >latest_num):
                    latest_num = the_ind
        if nums_checked == 5:
            if latest_num < earliest_winner:
                earliest_winner = latest_num
                winning_board = board

sum_of_unmarked = 0
numbers_called = bingo_nums[:earliest_winner+1]

for i in range(5):
    for j in range(5):
        item = winning_board[i][j]
        if item in numbers_called:
            pass
        else:
            sum_of_unmarked += item
            
        

last_number = bingo_nums[earliest_winner]
print("Winning number:", last_number)

print("Sum of Unmarked:", sum_of_unmarked)
print("Puzzle answer:", sum_of_unmarked *last_number)
