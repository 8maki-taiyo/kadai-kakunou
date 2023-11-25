n = int(input())
A = list(map(int, input().split()))

print(max([i for i in A if i!=max(A)]))