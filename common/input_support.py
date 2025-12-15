import requests

def get_session_text(year, day, cookies):
    """
    Fetches the input data from Advent of Code for a specific day and year.

    Args:
        year (int): The year of the Advent of Code event
        day (int): The day number of the challenge
        cookies (str): The session cookie value for authentication

    Returns:
        str: The raw input text from the Advent of Code website

    """
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": cookies}

    response = requests.get(url, cookies=cookies)
    return response.text

def create_file(input_type, text):
    """Writes text content to a file with the specified type as the base name.

    Args:
        input_type: The base name for the output file (without extension).
        text: The text content to write to the file.
    """
    with open(f"{input_type}.txt", "w") as f:
        f.write(text)

def create_input_file(text):
    """Creates an input.txt file with the provided text.

    This is a convenience wrapper around create_file() specifically for creating
    input files with the standard 'input.txt' filename.

    Args:
        text: The text content to write to input.txt
    """
    create_file("input", text)

def create_example_file(text):
    """Creates an example.txt file with the provided text.

    This is a convenience wrapper around create_file() specifically for creating
    example input files with the standard 'example.txt' filename.

    Args:
        text: The text content to write to example.txt
    """
    create_file("example", text)