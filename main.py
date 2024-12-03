import csv

import day1
import day2
import day3

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

def read_txt(txtfilename):
    f = open(txtfilename, "r")
    return f.readlines()

days = [day1, day2, day3]

if __name__ == "__main__":
    inp = input()
    day, part = inp.split()
    # data = read_csv("input/day" + day + ".csv")
    data = read_txt("input/day" + day + ".txt")
    day = int(day) - 1
    part = int(part)

    # ans = days[day].solution(data)
    
    if part == 1:
        ans = days[day].part_one(data)
    else: 
        ans = days[day].part_two(data)
    print(ans)