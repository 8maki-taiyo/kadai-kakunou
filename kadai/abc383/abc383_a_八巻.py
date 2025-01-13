def main():
    N = int(input())
    humidifier = 0
    last_time = 0
    
    for _ in range(N):
        time, water = map(int, input().split())
        
        # timeの加湿機中の水の量を求める(前回の水の量から経過時間分引く)
        humidifier = max(0, humidifier - (time - last_time))
        # 水追加
        humidifier += water
        last_time = time
        
    print(humidifier)
    
if __name__ == "__main__":
    main()