# https://dmoj.ca/problem/ccc00s4

distance, count = int(input()), int(input())
clubs = sorted([int(input()) for _ in range(count)])





# distance, count = int(input()), int(input())
# clubs = sorted([int(input()) for _ in range(count)], reverse=True)
# mem = {}
#
#
# def solve(d, c):
#     if d == 0: return 0
#     if c == len(clubs): return -1
#
#     key = f"{d},{c}"
#     if key in mem:
#         return mem[key]
#
#     t_count = d // clubs[c]
#     t_val = t_count * clubs[c]
#
#     for _ in range(t_count + 1):
#         val = solve(d - t_val, c + 1)
#         if val > -1:
#             mem[key] = val + t_count
#             return mem[key]
#         t_val -= clubs[c]
#         t_count -= 1
#
#     mem[key] = -1
#     return mem[key]
#
#
# calc = solve(distance, 0)
# if calc > -1:
#     print(f"Roberta wins in {calc} strokes.")
# else:
#     print("Roberta acknowledges defeat.")