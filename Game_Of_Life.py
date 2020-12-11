import random, time
from copy import copy, deepcopy

# returns matrix of all 0s
def dead_state(width, height):
    board_state = []
    for i in range(height):
        board_state.append([0]*width)

    return board_state


# returns matrix (2D list)
def random_state(width, height):
    board_state = dead_state(width, height)

    for row in range(height):
        for col in range(width):
            random_number = random.random()
            if random_number >= 0.5:
                board_state[row][col] = 0
            else:
                board_state[row][col] = 1

    return board_state

# returns matrix into an actual visual "board"
def render(board_state):
    for row in range(height):
        print("|", end=" ")
        for col in range(width):
            if board_state[row][col] == 0:
                print(" ", end=" ")
            elif board_state[row][col] == 1:
                print("#", end=" ")
        print("|")


# returns number of live neighbors of a given cell on the board
def get_live_neighbors(initial_board_state, row, col):
    num_live_neighbors = 0
    # 8 possible neighbors
    try:
        if (row - 1) >= 0 and (col - 1) >= 0:
            if initial_board_state[row - 1][col - 1] == 1:
                num_live_neighbors += 1
            else:
                pass
    except:
        pass
    try:
        if (row - 1) >= 0:
            if initial_board_state[row - 1][col] == 1:
                num_live_neighbors += 1
            else:
                pass
    except:
        pass
    try:
        if (row - 1) >= 0:
            if initial_board_state[row - 1][col + 1] == 1:
                num_live_neighbors += 1
            else:
                pass
    except:
        pass
    try:
        if (col - 1) >= 0:       
            if initial_board_state[row][col - 1] == 1:
                num_live_neighbors += 1
            else:
                pass
    except:
        pass
    try:
        if initial_board_state[row][col + 1] == 1:
            num_live_neighbors += 1
        else:
            pass
    except:
        pass
    try:
        if (col - 1) >= 0:
            if initial_board_state[row + 1][col - 1] == 1:
                num_live_neighbors += 1
            else:
                pass
    except:
        pass
    try:
        if initial_board_state[row + 1][col] == 1:
            num_live_neighbors += 1
        else:
            pass
    except:
        pass
    try:
        if initial_board_state[row + 1][col + 1] == 1:
            num_live_neighbors += 1
        else:
            pass
    except:
        pass

    return num_live_neighbors


# returns next board version based on the rules of life
def next_board_state(initial_board_state):
    new_board_state = deepcopy(initial_board_state)
    # iterate through all cells
    # if statements for 4 conditions
    for row in range(len(initial_board_state)):
        for col in range(len(initial_board_state[0])):
            if initial_board_state[row][col] == 1: # cell is alive
                # if live neighbors = 0, 1, or >3, becomes dead
                if ((get_live_neighbors(initial_board_state, row, col) == 0) or
                (get_live_neighbors(initial_board_state, row, col) == 1) or
                (get_live_neighbors(initial_board_state, row, col) > 3)):
                    new_board_state[row][col] = 0

                # elif 2 or 3 live neighbors, continue
                elif (initial_board_state[row][col] == 2) or (initial_board_state[row][col] == 3):
                    pass

            elif initial_board_state[row][col] == 0: # cell is dead
                # if live neighbors = 3, becomes alive
                if (get_live_neighbors(initial_board_state, row, col) == 3):
                    new_board_state[row][col] = 1
                # else continue
                else:
                    pass

    return new_board_state

# imports data from text file and and returns board state
def load_board_state(file_name):
    file = open(file_name)
    data = file.read().splitlines()
    data_list = []
    for i in data:
        data_list.append(list(i))
    new_data_list = []
    for row in data_list:
        new_row = [int(i) for i in row]
        new_data_list.append(new_row)
    
    return new_data_list


# MAIN
width = 40
height = 12


# initial_board_state = random_state(width,height)
initial_board_state = load_board_state("Gospel_Glider_Gun.txt")

new_board_state = next_board_state(initial_board_state)

render(new_board_state)

while True:
    new_board_state = next_board_state(new_board_state)
    time.sleep(.25)
    render(new_board_state)

