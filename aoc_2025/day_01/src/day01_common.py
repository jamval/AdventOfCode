from common.input_support import *

#region Input Handling

def get_puzzle_input():
    if not inputs_file_exits():
        text = get_session_text(2025, 1, "53616c7465645f5f116211ebfe92fbe3a2d174d0fef016d518e5dec47cce27d5a843dade9d9767e8890502fe0c16774739b59c0c8d27022644221bf8a988ed8d")
        create_input_file(text)

#endregion Input Handling