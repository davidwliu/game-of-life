from Game_Of_Life import next_board_state, get_live_neighbors

# TODO: there's a lot of repeated code here. Can
# you move some of into reusable functions to
# make it shorter and neater?

def do_test(expected_state, actual_state, test_number):
    if expected_state == actual_state:
        print("PASSED " + str(test_number))
    else:
        print("FAILED " + str(test_number) + "!")
        print("Expected:")
        print(expected_state)
        print("Actual:")
        print(actual_state)

if __name__ == "__main__":

    # TEST 1: dead cells with no live neighbors
    # should stay dead.
    test_number = 1

    init_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    actual_next_state1 = next_board_state(init_state1)
    do_test(expected_next_state1, actual_next_state1, test_number)


    # TEST 2: dead cells with exactly 3 neighbors
    # should come alive.
    test_number = 2

    init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    actual_next_state2 = next_board_state(init_state2)
    do_test(expected_next_state2, actual_next_state2, test_number)


    # TEST 3: any live cell with 0 or 1 live neighbors becomes dead
    test_number = 3

    init_state3 = [
        [1,0,0],
        [0,0,1],
        [0,0,1]
    ]
    expected_next_state3 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    actual_next_state3 = next_board_state(init_state3)
    do_test(expected_next_state3, actual_next_state3, test_number)


    # TEST 4: any live cell 2 or 3 live neighbors stays alive
    test_number = 4

    init_state4 = [
        [1,1,0],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state4 = [
        [1,1,1],
        [1,0,1],
        [0,0,0]
    ]
    actual_next_state4 = next_board_state(init_state4)
    do_test(expected_next_state4, actual_next_state4, test_number)

    # TEST 5: any live cell with more than 3 live neighbors becomes dead
    test_number = 5

    init_state5 = [
        [1,1,0],
        [0,1,1],
        [0,0,1]
    ]
    expected_next_state5 = [
        [1,1,1],
        [1,0,1],
        [0,1,1]
    ]
    actual_next_state5 = next_board_state(init_state5)
    do_test(expected_next_state5, actual_next_state5, test_number)