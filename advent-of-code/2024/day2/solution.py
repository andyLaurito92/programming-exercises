"""
Part 1
"""

def issafe(levels: list[int]) -> (bool, int):
    isincreasing = lambda num1, num2: num1 < num2
    difference = lambda num1, num2: abs(num1 - num2) < 4 

    for i in range(1, len(levels)):
        if i == 1:
            if levels[0] > levels[1]:
                isincreasing = lambda num1, num2: num1 > num2
        if not (isincreasing(levels[i-1], levels[i]) and difference(levels[i-1], levels[i])):
            return False, i
    return True, -1
    

safe_reports = 0
with open("input.txt") as reports:
    for report in reports.readlines():
        levels = list(map(int, report.split()))
        res, level_breaks = issafe(levels)
        if res:
            safe_reports += 1

print(safe_reports)



"""
Part 2
"""

def issafeToleratingBadLevel(levels: list[int]) -> bool:
    """
    The trick here is to realize that you need to check not just the ith level
    that breaks, but actually 2 more back. This is kind of a "narrowed" brute
    force algorithm
    """
    level_safe, i = issafe(levels)
    if level_safe:
        return True
    else:
        levels_without_i = levels[:i] + levels[i+1:]
        levels_without_iminus1 = levels[:i-1] + levels[i:]
        minus2res = False
        if i >= 2:
            levels_without_iminus2 = levels[:i-2] + levels[i-1:]
            #print(levels_without_iminus2)
            minus2res = issafe(levels_without_iminus2)[0]
        return issafe(levels_without_i)[0] or issafe(levels_without_iminus1)[0] or minus2res
        


assert False == issafeToleratingBadLevel([1, 2, 7, 8, 9])
assert True == issafeToleratingBadLevel([7, 6, 5, 2, 1])
assert False == issafeToleratingBadLevel([9, 7, 6, 2, 1])
assert True == issafeToleratingBadLevel([1, 3, 2, 4, 5])
assert True == issafeToleratingBadLevel([8, 6, 4, 4, 1])
assert True == issafeToleratingBadLevel([1, 3, 6, 7, 9])
assert False == issafeToleratingBadLevel([32, 32, 32, 30, 27, 26, 22])

assert False == issafeToleratingBadLevel([38, 40, 38, 37, 37, 37])
assert False == issafeToleratingBadLevel([20, 20, 21, 23, 26, 27, 27])
assert True == issafeToleratingBadLevel([7, 8, 9, 12, 12])
assert True == issafeToleratingBadLevel([8, 4, 3, 2, 1])
assert True == issafeToleratingBadLevel([1, 2, 3, 5, 8, 33])
assert True == issafeToleratingBadLevel([1, 6, 2])
assert True == issafeToleratingBadLevel([4, 5, 3, 6])
assert True == issafeToleratingBadLevel([71, 69, 70, 71, 72, 75])
#[72, 71, 69, 70, 71, 72, 75]


safe_reports = 0
total_reports = 0
with open("input.txt") as reports:
    for report in reports.readlines():
        total_reports += 1
        levels = list(map(int, report.split()))
        if issafeToleratingBadLevel(levels):
            safe_reports += 1

print(safe_reports, total_reports)
