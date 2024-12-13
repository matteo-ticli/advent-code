from utils import load_txt


def summation_mul(l: list) -> int:
    tot = 0
    for i in l:
        tot += i[0] * i[1]
    return tot


def compose_number(match: str, i: int):
    num = ""
    i += 1
    while True:
        try:
            int(match[i])
            num += match[i]
            i += 1
            if match[i] == ",":
                X = int(num)
                num = ""
                i += 1
                while True:
                    try:
                        int(match[i])
                        num += match[i]
                        i += 1
                        if match[i] == ")":
                            Y = int(num)
                            return X, Y
                    except:
                        return 0, 0
        except:
            return 0, 0


def find_match(m: str, i: int, match: str = "mul(X,Y)"):
    j = 0
    while i < len(m):
        if m[i] == match[j]:
            if match[j+1] == "(":
                i += 1 # skip (
                return compose_number(m, i)
            i += 1
            j += 1
        else:
            return 0, 0


def mul_flag(m: str, i: int, do: str = "do()", dn: str = "don't()"):
    len_m, len_do, len_dn = len(m), len(do), len(dn)
    try:
        if m[i:i+len_do] == do:
            return "do"
        elif m[i:i+len_dn] == dn:
            return "do_not"
    except:
        return None


def day_3_1(s: str):
    mul_container = []
    for i in range(len(s)):
        if i == len(s) - 1:
            break
        else:
            if s[i] == "m":
                mul_container.append(find_match(s, i))
    return summation_mul(mul_container)


def day_3_2(s: str):
    mul_container = []
    do_flag = "do"
    for i in range(len(s)):
        if s[i] == "m":
            if do_flag=="do":
                mul_container.append(find_match(s, i))
        elif s[i] == "d":
            if mul_flag(s, i) is not None:
                do_flag = mul_flag(s, i)
    return summation_mul(mul_container)


# test_1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
# test_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
str_03 = load_txt("day_3.txt")

print(f'Solution 3.1 : {day_3_1(str_03)}')
print(f'Solution 3.2 : {day_3_2(str_03)}')