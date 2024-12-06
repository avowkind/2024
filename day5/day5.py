"""
Advent of Code 2024: Day 5 - Print order


"""

import os

rules = []
manuals = []


def parser(file_path):
    """
    Generator that returns one array of integers per line at a time.

    :param file_path: Path to the input file.
    :return: Yields a list of integers for each line in the file.
    """
    local_rules: list = []
    local_prints: list = []
    reading_rules = True
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip() == "":
                reading_rules = False
                continue
            if reading_rules:
                local_rules.append(line.strip())
            else:
                local_prints.append(line.strip())
    # convert rules from nn|nn to (nn, nn)
    local_rules = [rule.split("|") for rule in local_rules]
    local_rules = [(int(rule[0]), int(rule[1])) for rule in local_rules]
    # convert prints from string to int array
    local_prints = [list(map(int, print_line.split(','))) for print_line in local_prints]             
    return local_rules, local_prints

def check_order(page):
    """
    Check if the given print is in correct order based on the rules.
    """
    for rule in rules:
        if rule[0] in page and rule[1] in page:
            if page.index(rule[0]) > page.index(rule[1]):
                return False
    return True
    
def not_check_order(page):
    return not check_order(page)

def reorder(page):
    """
    Reorder the print based on the rules.
    """
    changed = True
    while changed:
        changed = False
        for rule in rules:
            if rule[0] in page and rule[1] in page:
                if page.index(rule[0]) > page.index(rule[1]):
                    page[page.index(rule[0])], page[page.index(rule[1])] = page[page.index(rule[1])], page[page.index(rule[0])]
                    changed = True
    return page

def main(file_path):
    global rules, manuals
    rules, manuals  = parser(file_path)
    ordered_manuals = list(filter(check_order, manuals))
    # print(ordered_manuals)
    # collect array of the middle element of each manual
    middle_elements = [manual[len(manual) // 2] for manual in ordered_manuals]
    print(middle_elements)
    print(sum(middle_elements))

    # part two
    unordered_manuals = list(filter(not_check_order, manuals))
    print(unordered_manuals)
    reordered = list(map(reorder, unordered_manuals))
    print(reordered)
    middle_elements = [manual[len(manual) // 2] for manual in reordered]
    print(middle_elements)
    print(sum(middle_elements))


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    input_file_path = os.path.join(script_dir, "input.txt")
    main(input_file_path)