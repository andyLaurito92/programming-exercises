"""
Part 1
"""

def issafe(levels: list[int]) -> bool:
    isincreasing = lambda num1, num2: num1 < num2
    difference = lambda num1, num2: abs(num1 - num2) < 4 

    for i in range(1, len(levels)):
        if i == 1:
            if levels[0] > levels[1]:
                isincreasing = lambda num1, num2: num1 > num2
        if not (isincreasing(levels[i-1], levels[i]) and difference(levels[i-1], levels[i])):
            return False
    return True
    

safe_reports = 0
with open("input.txt") as reports:
    for report in reports.readlines():
        levels = list(map(int, report.split()))
        if issafe(levels):
            safe_reports += 1

print(safe_reports)



"""
Part 2
"""

def issafeToleratingBadLevel(levels: list[int]) -> bool:
    isincreasing = lambda num1, num2: num1 < num2
    difference = lambda num1, num2: abs(num1 - num2) < 4 

    first_bad_level = True
    i = 1
    j = 0
    toskip = -1
    while i < len(levels):
        if i == 1:
            if levels[0] > levels[1]:
                isincreasing = lambda num1, num2: num1 > num2
        if not (isincreasing(levels[j], levels[i]) and difference(levels[j], levels[i])):
            if first_bad_level:
                first_bad_level = False
                i += 1
                toskip = i
            else:
                return False
        else:
            i += 1
            j += 1
            if j == toskip:
                j += 1
    return True


assert False == issafeToleratingBadLevel([1, 2, 7, 8, 9])
assert True == issafeToleratingBadLevel([7, 6, 5, 2, 1])
assert False == issafeToleratingBadLevel([9, 7, 6, 2, 1])
assert True == issafeToleratingBadLevel([1, 3, 2, 4, 5])
assert True == issafeToleratingBadLevel([8, 6, 4, 4, 1])
assert True == issafeToleratingBadLevel([1, 3, 6, 7, 9])

safe_reports = 0
with open("input.txt") as reports:
    for report in reports.readlines():
        levels = list(map(int, report.split()))
        if issafeToleratingBadLevel(levels):
            safe_reports += 1

print(safe_reports)
