"""
Advent of Code 2024: Day 2
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
            yield list(map(int, line.split()))


def safety_check(line: list[int]):
    """
    Check if the levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

    :param line: List of integer levels.
    :return: True if the line passes the safety check, False otherwise.
    """
    diffs = [y - x for x, y in zip(line, line[1:])]
    print(diffs)
    if not (all(d > 0 for d in diffs) or all(d < 0 for d in diffs)):
        print("Failed: All levels are either increasing or decreasing")
        return False

    if not all(1 <= abs(d) <= 3 for d in diffs):
        print("Failed: All differences are between 1 and 3")
        return False

    print("Passed")
    return True


def damped_safety_check(line: list[int]):
    """
    Check if the levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.
    If not, check if removing a single level makes the report safe.

    :param line: List of integer levels.
    :return: True if the line passes the damped safety check, False otherwise.
    """
    safe = safety_check(line)
    if safe:
        return True

    return problem_dampener(line)


def problem_dampener(line: list[int]):
    """
    Check if removing a single level from unsafe reports makes them safe.

    :param line: List of integer levels.
    :return: True if removing a single level makes the line safe, False otherwise.
    """
    for i, _ in enumerate(line):
        new_line = line[:i] + line[i + 1 :]
        if safety_check(new_line):
            print(f"Removed level {line[i]}")
            return True
    return False


def part1(lines):
    """
    Count the number of safe reports.

    :param lines: Generator of lists of integer levels.
    """
    results = [safety_check(line) for line in lines]
    # print(results)
    print(sum(results))


def part2(lines):
    """
    Count the number of safe reports with damped safety check.

    :param lines: Generator of lists of integer levels.
    """
    results = [damped_safety_check(line) for line in lines]
    print(results)
    print(sum(results))


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    input_file_path = os.path.join(script_dir, "input.txt")
    xlines = getline(input_file_path)
    # part1(xlines)
    part2(xlines)
