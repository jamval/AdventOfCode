from common.input_support import create_input_file, create_example_file

# region Constants

YEAR = "2025"
DAY = "01"

START_POINT = 50

LEFT = "L"
RIGHT = "R"

EXAMPLE_INPUT = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

# endregion Constants

#region Input Handling

def generate_puzzle_input():
    cookies = "53616c7465645f5f116211ebfe92fbe3a2d174d0fef016d518e5dec47cce27d5a843dade9d9767e8890502fe0c16774739b59c0c8d27022644221bf8a988ed8d"
    return create_input_file(YEAR, DAY, cookies)

def generate_example_input():
    return create_example_file(YEAR, DAY, EXAMPLE_INPUT)

#endregion Input Handling

# region Puzzle Solving

def solve_puzzle01(file_path):
    pos = START_POINT
    count = 0

    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line != "":
                direction = line[0]
                distance = int(line[1:])
                pos = turn_dial(pos, direction, distance)
                if pos == 0:
                    count += 1

    return count

def solve_puzzle02(file_path):
    pos = START_POINT
    count = 0

    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line != "":
                direction = line[0]
                distance = int(line[1:])

                count += count_zeroes(pos, direction, distance)
                pos = turn_dial(pos, direction, distance)

    return count

def turn_dial(pos, direction, distance):
    if direction == LEFT:
        return (pos - distance) % 100
    elif direction == RIGHT:
        return (pos + distance) % 100
    else:
        return pos

def count_zeroes(pos, direction, distance):
    zero_count = 0

    if direction == LEFT:
        if pos - distance > 0:
            return zero_count
        else:
            if pos != 0:
                distance -= pos
                zero_count += 1
    elif direction == RIGHT:
        if pos + distance < 100:
            return zero_count
        else:
            if pos != 0:
                distance = distance - (100 - pos)
                zero_count += 1
    else:
        print("Invalid operation")
        return zero_count

    return zero_count + distance // 100

# endregion Puzzle Solving