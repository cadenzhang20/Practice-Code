# https://dmoj.ca/problem/tc19summerf

from math import sqrt, floor

start = [int(x) for x in input().split()]
end = [int(x) for x in input().split()]

dif = [abs(end[x] - start[x]) for x in range(3)]
dis = sqrt(sum([dif[x] ** 2 for x in range(3)]))

print(max(dif))
print(floor(dis))
print(sum(dif))
