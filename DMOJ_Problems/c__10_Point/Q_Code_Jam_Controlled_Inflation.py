# https://dmoj.ca/problem/gcj22r1bb

for c in range(int(input())):
    customer_count = int(input().split()[0])

    point_list = []
    for _ in range(customer_count):
        products = [int(x) for x in input().split()]

        min_val, max_val = products[0], products[0]
        for p in products[1:]:
            if p < min_val: min_val = p
            elif p > max_val: max_val = p
        
        point_list.append([min_val, max_val])

    tab_table = [[0 for _ in range(2)] for _ in range(customer_count)]
    for p in range(customer_count - 2, -1, -1):
        for n in 0, 1:
            tab_table[p][n] = min([abs(point_list[p][n] - point_list[p + 1][1 - x]) + tab_table[p + 1][x] for x in (0, 1)])

    base_val = point_list[0][0] + sum([points[1] - points[0] for points in point_list])
    print(f"Case #{c + 1}: {tab_table[0][1] + base_val}")
