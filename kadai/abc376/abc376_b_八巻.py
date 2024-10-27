def main():
    N, Q=map(int,input().split())
    L, R = 1, 2
    ans = 0
    for _ in range(Q):
        H, T = input().split()
        T = int(T) 
        
        if H == "L":
            to = (T - L) % N
            ng = (R - L) % N
            # 基本は時計回りで移動させた場合で考えるが、その間にもう片方の腕がある場合反時計回りで移動させる
            if ng < to:
                ans += N - to
            else:
                ans += to
            L = T
        else:
            to = (T - R) % N
            ng = (L - R) % N
            if ng < to:
                ans += N - to
            else:
                ans += to
            R = T
    print(ans)

if __name__ == "__main__":
    main()