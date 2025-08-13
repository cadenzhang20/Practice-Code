# https://dmoj.ca/problem/ccc03s3
# Thu Jul 4

tiles = int(input())
rows = int(input())
cols = int(input())

grid = [["I"] + list(input()) + ["I"] for _ in range(rows)]
grid.insert(0, ["I"] * (cols + 2))
grid.append(["I"] * (cols + 2))

queue_grid = [[0 for _ in range(cols + 2)] for _ in range(rows + 2)]


def room_find(y, x):
    global queue_grid

    if grid[y][x] == "I" or queue_grid[y][x] == 1:
        return 0
    queue_grid[y][x] = 1

    return 1 + room_find(y, x + 1) + room_find(y - 1, x) + room_find(y, x - 1) + room_find(y + 1, x)


rooms = []
for r in range(1, rows + 1):
    for c in range(1, cols + 1):
        if grid[r][c] == "." and queue_grid[r][c] == 0:
            rooms.append(room_find(r, c))

rooms.sort(reverse=True)
tiled_rooms = 0
while rooms:
    if tiles >= rooms[0]:
        tiled_rooms += 1
        tiles -= rooms[0]
        rooms.pop(0)
    else:
        break

one_room_condition = "" if tiled_rooms == 1 else "s"
print(f"{tiled_rooms} room{one_room_condition}, {tiles} square metre(s) left over")
