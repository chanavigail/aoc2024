def part_one(rows):
    ans = 0
    for row in rows:
        row = row.split()
        
        check1 = int(row[1]) - int(row[0])  # 2nd term - 1st term
        if abs(check1) >= 1 and abs(check1) <= 3:       # safety 2
            inc = 1 if check1 > 0 else 0
        else: 
            continue

        for i in range(1, len(row) - 1):
            diff = int(row[i + 1]) - int(row[i])
            check2 = (diff > 0 and inc) or (diff < 0 and not inc)   # safety 1
            check3 = abs(diff) >= 1 and abs(diff) <= 3              # safety 2
            if check2 and check3:
                if i == len(row) - 2: ans += 1
                continue
            else: 
                break
    
    return ans

def part_two(rows):
    def dampen(row):
        for i in range(len(row)):
            row2 = row.copy()
            row2.pop(i)
            safe = checker(row2)
            if safe: return True
        return False

    def checker(row):
        check1 = int(row[1]) - int(row[0])  # 2nd term - 1st term
        if abs(check1) >= 1 and abs(check1) <= 3:       # safety 2
            inc = 1 if check1 > 0 else 0
        else:
            return False
        
        for i in range(len(row) - 1):
            diff = int(row[i + 1]) - int(row[i])
            check2 = (diff > 0 and inc) or (diff < 0 and not inc)   # safety 1
            check3 = abs(diff) >= 1 and abs(diff) <= 3              # safety 2
            if check2 and check3:
                continue
            else: return False
        return True

    ans = 0
    for row in rows:
        row = row.split()
        
        v1 = checker(row)
        if v1: ans += 1
        else: 
            v2 = dampen(row)
            if v2: ans += 1

    return ans

import csv
def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []

    with open(csvfilename, encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row[0])
    return rows

d = read_csv("./input/test.csv")
# d = read_csv("./input/day2.csv")
# part_one(d)
part_two(d)