def main():
    S = input()
    ans = []
    count = 0

    for i in range(1, len(S)):
        if S[i] == "|":
            ans.append(count)
            count = 0
        else:
            count += 1
    print(*ans)

if __name__ == "__main__":
    main()