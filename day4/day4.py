"""
Advent of Code 2024: Day 4 - Word search

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX

Find the count of the word "XMAS" in the word search.
words can go in any direction (up, down, left, right, diagonal) and can overlap.

"""

import os


def getline(file_path):
    """
    Generator that returns one array of integers per line at a time.

    :param file_path: Path to the input file.
    :return: Yields a list of integers for each line in the file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()


def find_xmas(grid):
    """
    Find the count of the word "XMAS" in the word search.
    Words can go in any direction (up, down, left, right, diagonal) and can overlap.
    """

    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    def check_direction(x, y, dx, dy, pattern):
        if not pattern:  # Found complete word
            return 1

        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == pattern[0]:
            return check_direction(nx, ny, dx, dy, pattern[1:])
        return 0

    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "X":
                # Try each direction for 'MAS'
                for dx, dy in directions:
                    count += check_direction(i, j, dx, dy, "MAS")

    return count


def find_x_mas(grid):
    """
    Find the count of the pattern matching MAS in a cross in the word search grid
    start by finding an A,
    then check for M in all of the 4 corner directions
    if found check for S in the same direction on other side
    then check for M in the remaining 2 directions and
    again check for S in the same direction on other side
    """
    rows = len(grid)
    cols = len(grid[0])
    corners = [(-1, -1), (1, -1), (-1, 1), (1, 1)]

    count = 0
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                continue
            if grid[i][j] == "A":
                # Try each direction for 'M'
                mas_found = 0
                for dx, dy in corners:
                    if grid[i + dx][j + dy] == "M":
                        # check for S on the opposite side
                        if grid[i - dx][j - dy] == "S":
                            mas_found += 1
                if mas_found == 2:
                    count += 1

    return count


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    input_file_path = os.path.join(script_dir, "input.txt")
    xlines = getline(input_file_path)
    # convert lines to a grid
    wordsearch = [list(line) for line in xlines]
    ## part 1
    print(find_xmas(wordsearch))

    ## part 2
    print(find_x_mas(wordsearch))