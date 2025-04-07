"""
Part 1
"""

import re


MULTIPLY_REGEX = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

def read(path):
    with open(path) as input_file:
        corrupted_memory = input_file.read()
    return corrupted_memory


memory_dump = read("input.txt")
res = 0
for x, y in MULTIPLY_REGEX.findall(memory_dump):
    res += int(x) * int(y)

print(res)


"""
Part 2
"""

MULTIPLY_REGEX_SECOND_PART = re.compile(r'(?!don\'t)mul\((\d{1,3}),(\d{1,3})\)')


test2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
