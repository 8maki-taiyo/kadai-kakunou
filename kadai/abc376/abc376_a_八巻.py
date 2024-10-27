def main():
    N,interval=map(int,input().split())
    push_time_list=list(map(int,input().split()))
    
    last_push_time = -interval
    ans = 0
    
    for push_time in push_time_list:
        # 最後にボタンを押した時間 - ボタンを押した時間 >= intarval だった場合 ans を更新して最後にボタンを押した時間を更新する
        if push_time - last_push_time >= interval:
            ans += 1
            last_push_time = push_time
    
    print(ans)
    
if __name__ == "__main__":
    main()