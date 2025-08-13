# https://dmoj.ca/problem/ccc07s4

from collections import defaultdict

point_count = int(input())
point_list = [0] * point_count
paths_dict = defaultdict(list)

while True:
    begin, end = [int(x) for x in input().split()]
    if begin == 0: break

    paths_dict[begin].append(end)

point_list[0] = 1

for p in range(point_count):
    for end in paths_dict[p + 1]:
        point_list[end - 1] += point_list[p]

print(point_list[-1])
