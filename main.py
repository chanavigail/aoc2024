import csv

import day1

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

days = [day1]

if __name__ == "__main__":
    day = input()
    data = read_csv("input/day" + day + ".csv")
    ans = days[int(day) - 1].solution(data)
    print(ans)