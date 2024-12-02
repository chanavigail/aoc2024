import csv

import day1
import day2

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

days = [day1, day2]

if __name__ == "__main__":
    day = input()
    data = read_csv("input/day" + day + ".csv")
    day = int(day) - 1

    part = input()
    part = int(part)

    # ans = days[day].solution(data)
    
    if part == 1:
        ans = days[day].part_one(data)
    else: 
        ans = days[day].part_two(data)
    print(ans)