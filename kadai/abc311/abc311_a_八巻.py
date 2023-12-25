max_m, max_d = map(int, input().split())
y, m, d = map(int, input().split())

d += 1
if d > max_d:
    d = 1
    m += 1
    if m > max_m:
        m = 1
        y += 1
print(y,m,d)