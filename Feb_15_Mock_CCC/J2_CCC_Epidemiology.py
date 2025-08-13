t, s, g = [int(input()) for _ in range(3)]
d = 0
nt = s

while nt <= t:
    s *= g
    nt += s
    d += 1

print(d)
