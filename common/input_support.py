import requests
import os

# TODO: Add docstrings

# region Constants

INPUTS_DIR = "inputs"

EXAMPLE = "example"
INPUT = "input"

EXAMPLE_FILE = "example.txt"
INPUT_FILE = "input.txt"

# endregion Constants

# region Input Fetching

def get_session_text(year, day, cookies):
    if day[0] == "0":
        day = day[1]

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": cookies}

    response = requests.get(url, cookies=cookies)
    return response.text

# endregion Input Fetching

# region File Path Handling

def get_inputs_path():
    current_dir = os.getcwd()
    parent_dir = current_dir.rsplit('\\', 1)[0]
    return os.path.join(parent_dir, INPUTS_DIR)

def get_examples_path(year, day):
    current_dir = os.getcwd()
    return current_dir + f"\\aoc_{year}\\day_{day}\\{INPUTS_DIR}"

def check_directory_exists(inputs_dir):
    if not os.path.exists(inputs_dir):
        try:
            os.makedirs(inputs_dir)
            return True
        except OSError as e:
            print(f"Failed to create inputs directory: {e}")
            return False
    return True

# endregion File Path Handling

# region File Creation

def create_input_file(year, day, session_cookies):
    directory_path = get_inputs_path()
    if not check_directory_exists(directory_path):
        return ""

    file_path = os.path.join(directory_path, INPUT_FILE)

    if not os.path.exists(file_path):
        text = get_session_text(year, day, session_cookies)
        create_file(file_path, text)

    return file_path

def create_example_file(year, day, text):
    directory_path = get_examples_path(year, day)
    if not check_directory_exists(directory_path):
        return ""

    file_path = os.path.join(directory_path, EXAMPLE_FILE)

    if not os.path.exists(file_path):
        create_file(file_path, text)

    return file_path

def create_file(file_path, text):
    with open(file_path, "w") as f:
        f.write(text)

# endregion File Creation