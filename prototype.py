from functools import reduce 

input = open("input.txt").read()
lines = input.split("\n")
reports = [[int(num) for num in line.split(" ")] for line in lines]

def checkReport(report):
    diff = report[1] - report[0]
    if (abs(diff) < 1 or abs(diff) > 3):
        return False
    for i in range(1, len(report) - 1):
        lastDiff = diff
        diff = report[i + 1] - report[i]
        if (lastDiff > 0 and diff < 0):
            return False
        if (lastDiff < 0 and diff > 0):
            return False
        if (abs(diff) < 1 or abs(diff) > 3):
            return False
    return True

results = list(map(checkReport, reports))
successResults = list(filter(lambda result: result is True, results))
# print(successResults)
print(len(successResults))