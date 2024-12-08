from utils import load_data


def is_report_safe(r):
    incr = r[-1] > r[0]
    if incr:
        for i in range(1, len(r)):
            if not 1 <= r[i] - r[i-1] <= 3:
                return False
        return True
    else:
        for i in range(1, len(r)):
            if not -3 <= r[i] - r[i-1] <= -1:
                return False
        return True


def is_report_safe_exclude_level(r):
    if is_report_safe(r):
        return True
    else:
        for i in range(len(r)):
            if is_report_safe(r[:i] + r[i+1:]):
                return True
    return False


def day_2_1(file_name):
    data = load_data(file_name)
    safe_reports = 0
    for row in data:
        row = [int(i) for i in row[0].split()]
        if is_report_safe(row):
            safe_reports += 1
    return safe_reports


def day_2_2(file_name):
    data = load_data(file_name)
    safe_reports = 0
    for row in data:
        row = [int(i) for i in row[0].split()]
        if is_report_safe_exclude_level(row):
            safe_reports += 1
    return safe_reports


print(f'Solution 2.1 : {day_2_1("day_2.txt")}')
print(f'Solution 2.2 : {day_2_2("day_2.txt")}')