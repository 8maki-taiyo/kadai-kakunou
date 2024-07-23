def main():
    n = int(input())
    L = [0]*n
    R = [0]*n
    for i in range(n):
        L[i], R[i] = map(int, input().split())
    X = [L[j] for j in range(n)]
    # sは0までの距離
    s = sum(X)

    # 最小の組み合わせの合計の時点で0を超えていたら"NO"を出す
    if s > 0:
        print("No")
        exit()

    for k in range(n):
        # LとRの差、もしくは0になるまでに必要な数値をlistに入れる
        d = min(-s, R[k]-L[k])
        X[k] += d
        # list に追加した分だけ0までの距離が縮まる
        s += d

    if s == 0:
        print("Yes")
        print(*X)
    else:
        print("No")

    
if __name__ == "__main__":
    main()