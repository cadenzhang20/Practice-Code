# https://dmoj.ca/problem/ccc15j5

slices, people = int(input()), int(input())
mem = {}


def solve(n, k, t_min):
    if k == 1:
        return 1

    key = f"{n},{k},{t_min}"
    if key in mem:
        return mem[key]

    total = 0
    for x in range(t_min, (n // k) + 1):
        total += solve(n - x, k - 1, x)
    mem[key] = total
    return total


print(solve(slices, people, 1))
