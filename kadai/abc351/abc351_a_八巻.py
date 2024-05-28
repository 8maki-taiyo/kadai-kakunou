def main():
    a = [int(i) for i in (input().split())]
    b = [int(i) for i in (input().split())]
    
    # 条件を見てみると A1+A2...+A9 >= B1+B2...+B8 のためこれだけでよい 
    print(sum(a)-sum(b)+1)

if __name__ == "__main__":
    main()