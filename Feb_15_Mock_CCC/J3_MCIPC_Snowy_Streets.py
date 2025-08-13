bas, dire = input().split()
dire = 0 if dire == "ns" else 1

s = {bas: dire}

for _ in range(int(input())):
    old, new = input().split()
    s[new] = 0 if s[old] else 1

ns, ew = 0, 0
for val in s:
    if s[val]:
        ew += 1
    else:
        ns += 1

print(ns, ew)
