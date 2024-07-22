def main():
    n = int(input())
    L = [0]*n
    R = [0]*n
    for i in range(n):
        L[i], R[i] = map(int, input().split())
    T = 0
    X = [L[j] for j in range(n)]
    s = sum(X)

    if s > 0:
        print("No")
        exit()

    for k in range(n):
        d = min(T-s, R[k]-L[k])
        X[k] += d
        s += d

    if s == T:
        print("Yes")
        print(*X)
    else:
        print("No")

    
if __name__ == "__main__":
    main()