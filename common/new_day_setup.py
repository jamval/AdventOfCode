import os
from datetime import datetime

# region Entrypoint

def main():
    year = get_valid_year()
    if year == -1:
        return

    # todo: get valid day

    current_dir = os.getcwd()
    aoc_dir = current_dir.rsplit('\\', 1)[0]
    print(aoc_dir)
    pass

if __name__ == "__main__":
    main()

# endregion Entrypoint

# region Constants

YEAR_DIR_NAME = "aoc_"
DAY_DIR_NAME = "day_"

# endregion Constants

# region Functions

def get_valid_year():
    year = 0
    while (not year.isdigit() or
           int(year) != -1 and
           (datetime.now().year + 1) >= int(year) >= 2015):

        year = input(f"Please enter a valid year (2015 - {datetime.now().year + 1})." + '/n' +
                     "If you wish to exit instead, enter -1." + '/n')
    return year

# endregion Functions


