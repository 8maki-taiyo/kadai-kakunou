def main():
    n, limit = map(int, input().split())
    hands = [int(i) for i in (input().split())]
    ans = 0
    
    for h in hands:
        limit -= h
        if limit < 0:
            break
        ans += 1    
    print(ans)

if __name__ == "__main__":
    main()