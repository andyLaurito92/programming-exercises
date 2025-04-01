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
