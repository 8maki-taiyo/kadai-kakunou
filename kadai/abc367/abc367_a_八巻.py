def main():
    A,B,C = map(int, input().split())
    
    # 0時をまたぐパターンとまたがないパターンの二つを作る
    if B < C:
        if B < A < C:
            print("No")
        else:
            print("Yes")
    else:
        if C < A < B:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()