arr = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

pos = [1, 1]

for x in range(2):
    for m in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        new_pos = [pos[0] + m[0], pos[1] + m[1]]
        arr[new_pos[0]][new_pos[1]] = 1

for li in arr:
    print(*li)
