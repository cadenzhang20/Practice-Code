a, b = list(map(int, input().split()))
print(max(a + b, abs(a - b), a * b))