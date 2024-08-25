def main():
    X = input()
    
    # 後ろ側の0を一つずつ消していく
    while X[-1] == "0":
        X = X[:-1]
        # 整数になったらループをぬける
        if X[-1] == ".":
            X = X[:-1]
            break
    
    print(X)

if __name__ == "__main__":
    main()