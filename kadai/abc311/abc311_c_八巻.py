N = int(input())
A = list(map(int,input().split()))
sort_A = A.sort()
ans = []

for a in A:
    sum = 0
    for _a in A:
        if a < _a:
            sum += _a
    ans.append(sum)
    
print(*ans)
