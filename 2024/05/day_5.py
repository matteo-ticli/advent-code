from utils import *
import os


def load_data(file_name):
    # Set directory path
    os.chdir("/Users/matteoticli/Projects_Personal/advent-code/advent-code/2024/05/")

    # Load Data
    data = load_txt(file_name)
    data_cleaned = data.strip('|').strip().split('\n')

    data_final = []
    for item in data_cleaned:
        if '|' in item:
            data_final.append(list(map(int, item.split('|'))))
        elif item == "":
            data_final.append([])
        else:
            data_final.append(list(map(int, item.split(','))))

    # Divide data into "page_order" and "rules"
    pos_for_split = data_final.index([])
    page_order, rules = data_final[:pos_for_split], data_final[pos_for_split+1:]

    return page_order, rules


def find_mid_value_pt1(data):
    page_order = data[0]
    rules = data[1]

    # Check rules that follow the correct page ordering
    rules_ok_cont = []
    for rule in rules:
        rule_ok = True
        for j, num in enumerate(rule):
            if not rule_ok:
                break
            if j == len(rule)-1:
                break
            for i in range(j+1, len(rule)):
                to_check = [num, rule[i]]
                if to_check not in page_order:
                    rule_ok = False
                    break
        if rule_ok:
            rules_ok_cont.append(rule)

    # Find mid-rule values and sum them up
    output = 0
    for r in rules_ok_cont:
        output += r[len(r)//2]

    return output


def find_mid_value_pt2(data):
    page_order = data[0]
    rules = data[1]

    # Check rules that follow the correct page ordering
    rules_not_ok_cont = []
    for rule in rules:
        rule_ok = True
        for j, num in enumerate(rule):
            if not rule_ok:
                break
            elif j == len(rule) - 1:
                break
            for i in range(j + 1, len(rule)):
                to_check = [num, rule[i]]
                if to_check not in page_order:
                    rule_ok = False
                    break
        if not rule_ok:
            rules_not_ok_cont.append(rule)

    del rule, rules, j, num, i, to_check

    # Find the correct ordering of the saved rules
    for rule in rules_not_ok_cont:
        for j in range(len(rule)):
            if j == len(rule)-1:
                break
            for i in range(j+1, len(rule)):
                to_check = [rule[j], rule[i]]
                if to_check not in page_order:
                    rule[j], rule[i] = rule[i], rule[j]


    # Find mid-rule values and sum them up
    output = 0
    for r in rules_not_ok_cont:
        output += r[len(r)//2]

    return output

print(f"Day5-pt1: {find_mid_value_pt1(load_data('day_5.txt'))}")
print(f"Day5-pt2: {find_mid_value_pt2(load_data('day_5.txt'))}")


