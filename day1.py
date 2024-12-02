def part_one(rows):
    left = []
    right = []

    for row in rows:
        a, b = row.split()
        left.append(int(a))
        right.append(int(b))
    
    left.sort()
    right.sort()

    ans = 0
    for i in range(len(left)):
        ans += abs(left[i] - right[i])

    return ans

def part_two(rows):

    left = []   # left list
    right = {}  # dict of k: number in right list, v: num appearances

    for row in rows:
        a, b = row.split()
        left.append(int(a))
        b = int(b)
        if b in right:
            right[b] += 1
        else: right[b] = 1
    
    ans = 0
    for l in left:
        if l in right.keys():
            ans += l * right[l]
    
    return ans