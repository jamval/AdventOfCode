from day01_common import generate_puzzle_input, solve_puzzle01, solve_puzzle02

file_path = generate_puzzle_input()

answer = solve_puzzle01(file_path)
print(f"Answer to puzzle 01: {answer}")

answer = solve_puzzle02(file_path)
print(f"Answer to puzzle 02: {answer}")