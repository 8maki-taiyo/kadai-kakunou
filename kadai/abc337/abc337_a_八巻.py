N = int(input())
sum_x, sum_y = 0, 0

for i in range(N):
    x, y = map(int, input().split())
    sum_x += x
    sum_y += y

if sum_x > sum_y:
    print("Takahashi")
elif sum_x < sum_y:
    print("Aoki")
else:
    print("Draw")