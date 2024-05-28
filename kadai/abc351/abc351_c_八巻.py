def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = [a[0]]
    for i in range(1,n):
        ans.append(a[i])
        while len(ans) > 1 and ans[-1] == ans[-2]:
            ans[-2] += 1
            del ans[-1]
    print(len(ans))
    
if __name__ == "__main__":
    main()