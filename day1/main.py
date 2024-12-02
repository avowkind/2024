"""
Advent of Code 2024: Day 1
"""
import os

def read_input_file(file_path):
    array1 = []
    array2 = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            num1, num2 = map(int, line.split())
            array1.append(num1)
            array2.append(num2)
    return array1, array2


if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    input_file_path = os.path.join(script_dir, 'input.txt')
    a, b = read_input_file(input_file_path)
    a = sorted(a)
    b = sorted(b)
    print(a, b)

    ## Part 1
    # diff the two arrays
    diff = [abs(x - y) for x, y in zip(a, b)]
    print(diff)
    # sum the differences
    print(sum(diff))

    ## Part 2
    # find how often each item in a appears in 2.
    # create a dictionary of counts for each item in a
    counts = {}
    for item in b:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    print(counts)
    # for each item in a, if it appears in b, add the count * value to the sum
    sum2 = 0
    for item in a:
        if item in counts:
            sum2 += item * counts[item]
    print(sum2)

