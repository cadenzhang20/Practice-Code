# https://dmoj.ca/problem/ccc21j4
# Not completed

shelf = list(input())
swaps = 0

books = [0, 0, 0, 0]

for c in shelf:
    if c == "L":
        books[1] += 1
    elif c == "M":
        books[2] += 1
    elif c == "S":
        books[3] += 1

books[2] += books[1]
books[3] += books[2]

sects = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for b in range(3):
    print(*sorted(shelf[books[b]:books[b + 1]]))
    for c in shelf[books[b]:books[b + 1]]:
        if c == "L":
            sects[b][0] += 1
        elif c == "M":
            sects[b][1] += 1
        elif c == "S":
            sects[b][2] += 1

print(sects)

if sects[0][1] <= sects[1][0]:
    sects[0][0] += sects[1][0]
    sects[1][1] -= sects[1][0]

print(sects)


# # pairs = [["S", "L"], ["M", "L"], ["S", "M"]]
# pairs = [["S", "L"], ["S", "M"], ["M", "L"]]
#
# for le, gr in pairs:
#     left = 0
#     right = len(shelf) - 1
#
#     while left != right:
#         while left != right and shelf[left] != le:
#             left += 1
#         while left != right and shelf[right] != gr:
#             right -= 1
#         if left != right:
#             swaps += 1
#             shelf[left], shelf[right] = shelf[right], shelf[left]
#
#     # print("".join(shelf))

print(swaps)
