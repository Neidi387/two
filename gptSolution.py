def is_safe(report):
    """
    Determine if a report is safe based on the given rules.
    A report is safe if:
    1. The levels are either all increasing or all decreasing.
    2. Any two adjacent levels differ by at least 1 and at most 3.
    """
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    
    # Check if all differences are within the range [1, 3] or [-3, -1]
    if all(1 <= diff <= 3 for diff in differences):
        return True  # All increasing
    if all(-3 <= diff <= -1 for diff in differences):
        return True  # All decreasing
    return False  # Mixed or invalid differences

def count_safe_reports(data):
    """
    Count the number of safe reports in the data.
    Each line of data contains a report.
    """
    safe_count = 0
    for line in data:
        report = list(map(int, line.split()))
        if is_safe(report):
            safe_count += 1
    return safe_count

# Example input data (as described in the puzzle)
input = open("input.txt").read()
data = input.split("\n")
# data = [
#     "7 6 4 2 1",
#     "1 2 7 8 9",
#     "9 7 6 2 1",
#     "1 3 2 4 5",
#     "8 6 4 4 1",
#     "1 3 6 7 9"
# ]

# Process the data and count safe reports
safe_count = count_safe_reports(data)
print(f"Number of safe reports: {safe_count}")
