n, s, m, l = map(int, input().split())
price_list = []

for i in range(n + 1):
    for j in range(n + 1):
        for k in range(n + 1):
            if 6 * i + 8 * j + 12 * k >= n:
                price_list.append(i * s + j * m + k * l)
                
print(min(price_list))