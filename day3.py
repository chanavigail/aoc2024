import re

def part_one(rows):
    pattern = r"mul\((\d+),(\d+)\)"
    ans = 0
    for row in rows:
        valid = re.findall(pattern, row)
        for v in valid:
            ans += int(v[0]) * int(v[1])
    return ans

def part_two(rows):
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    rows = "".join(rows)
    # rows = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    instructions = re.findall(pattern, rows)
    do = True
    ans = 0
    for i in instructions:
        if i == "do()":
            do = True
        elif i == "don't()":
            do = False
        elif do:
            a, b = re.findall(r"\d+", i)
            ans += int(a) * int(b)
    return ans