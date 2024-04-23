def main():
    N, holiday, weekday = map(int, input().split())
    all_schedule = list(map(int,input().split()))
    youbi = set()
    
    # 予定が一週間の何日目かをset にいれる
    for schedule in all_schedule:
        youbi.add(schedule%(holiday+weekday))
        
    youbi = sorted(youbi)
    youbi.append(youbi[0]+ holiday + weekday)
    print(youbi)
    for i in range(len(youbi) - 1):
        if youbi[i + 1] - youbi[i] > weekday:
            print("Yes")
            exit()
    print("No")
    


if __name__ == "__main__":
    main()