"""
Advent of Code 2024: Day 3
"""

import os
import re

def getline(file_path):
    """
    Generator that returns one array of integers per line at a time.

    :param file_path: Path to the input file.
    :return: Yields a list of integers for each line in the file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()

def part1(text) -> int:
    """
    Parse the input line to find matches of mul(1,2) and return the sum of the products.

    :param text: Input text containing mul(a,b) patterns.
    :return: Sum of the products of the matched patterns.
    """
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    matches = re.findall(pattern, text)
    return sum(int(a) * int(b) for a, b in (re.findall(r'\d{1,3}', match) for match in matches))

def parse_symbols(text):
    """
    Parse mul(a,b), do(), and don't() symbols and return an array of the matches.

    :param text: Input text containing the symbols.
    :return: List of matched symbols.
    """
    pattern = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
    return re.findall(pattern, text)

def filter_symbols(matches):
    """
    Iterate across the matches and filter out symbols between don't() and do().

    :param matches: List of matched symbols.
    :return: Filtered list of symbols.
    """
    filtered_matches = []
    on = True
    for match in matches:
        if match == "do()":
            on = True
        elif match == "don't()":
            on = False
        elif on:
            filtered_matches.append(match)
    return filtered_matches

def do_muls(muls):
    """
    Iterate across the matches, extract the numbers, and return the sum of their products.

    :param muls: List of mul(a,b) matches.
    :return: Sum of the products of the matched patterns.
    """
    return sum(int(a) * int(b) for a, b in (re.findall(r'\d{1,3}', mul) for mul in muls))

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    input_file_path = os.path.join(script_dir, "input.txt")
    xlines = getline(input_file_path)
    symbols = [symbol for line in xlines for symbol in parse_symbols(line)]
    filtered_symbols = filter_symbols(symbols)
    result = do_muls(filtered_symbols)
    print(result)
