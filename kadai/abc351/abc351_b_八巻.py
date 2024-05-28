def main():
    n = int(input())
    a = [list(input()) for _ in range(n)]
    b = [list(input()) for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if a[i][j] != b[i][j]:
                print(i+1, j+1)
                exit()
    
if __name__ == "__main__":
    main()