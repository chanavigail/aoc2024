def part_one(rows):
    dims = len(rows)
    ans = 0
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for i in range(dims):
        for j in range(dims):
            if rows[i][j] == "X":
                for d in dirs:
                    if 0 <= i + 3 * d[0] < dims and 0 <= j + 3 * d[1] < dims:
                        ans += bool(
                            rows[i + d[0]][j + d[1]] == "M" and \
                            rows[i + 2 * d[0]][j + 2 * d[1]] == "A" and \
                            rows[i + 3 * d[0]][j + 3 * d[1]] == "S"
                        )
    return ans

def part_two(rows):
    dims = len(rows)
    ans = 0

    for i in range(dims):
        for j in range(dims):
            if rows[i][j] == "A" and 0 <= i - 1 and i + 1 < dims and 0 <= j - 1 and j + 1 < dims:
                ans += bool(
                    (rows[i - 1][j - 1] == "M" and rows[i - 1][j + 1] == "M" and rows[i + 1][j - 1] == "S" and rows[i + 1][j + 1] == "S") or 
                    (rows[i - 1][j - 1] == "S" and rows[i - 1][j + 1] == "S" and rows[i + 1][j - 1] == "M" and rows[i + 1][j + 1] == "M") or
                    (rows[i - 1][j - 1] == "M" and rows[i - 1][j + 1] == "S" and rows[i + 1][j - 1] == "M" and rows[i + 1][j + 1] == "S") or
                    (rows[i - 1][j - 1] == "S" and rows[i - 1][j + 1] == "M" and rows[i + 1][j - 1] == "S" and rows[i + 1][j + 1] == "M")
                    )
    return ans