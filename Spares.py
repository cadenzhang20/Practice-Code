from math import sqrt
start_num, end_num = int(input()), int(input())
g_len = int(-(sqrt(end_num + 1 - start_num) // -1))
grid = [[-1 for _ in range(g_len)] for _ in range(g_len)]
start = (g_len - 1) // 2

cur_num = start_num
pos = [start, start]
adder = 2
while cur_num <= end_num:
    for x, y in (1, 0), (1, 1), (-1, 0), (-1, 1):
        for _ in range(adder // 2):
            if cur_num > end_num: break
            else: grid[pos[0]][pos[1]], pos[y], cur_num = cur_num, pos[y] + x, cur_num + 1
        if cur_num > end_num: break
        else: adder += 1

[print(*["" if grid[x][y] == -1 else grid[x][y] for y in range(g_len)]) for x in range(g_len)]