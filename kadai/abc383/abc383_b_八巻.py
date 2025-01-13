# 全探索する
def main():
    h,w,d = map(int,input().split())
    s = [list(input()) for _ in range(h)]
    max_wet_floor = 0

    for i1 in range(h):
        for j1 in range(w):
            # 机マスは実行しない
            if s[i1][j1] != '#':

                for i2 in range(h):
                    for j2 in range(w):
                        # 机マスか同じ位置に2つの加湿器が同じ個所にある場合は実行しない
                        if not(s[i2][j2] == '#' or (i1 == i2 and j1 == j2)):
                            
                            # 原罪の加湿器の位置でどれだけの床が加湿されるか計算。最大値を記録
                            wet_floor = 0
                            for i in range(h):
                                for j in range(w):
                                    if s[i][j] != '#':
                                        if(abs(i-i1)+abs(j-j1))<=d:
                                            wet_floor += 1
                                        elif(abs(i-i2)+abs(j-j2))<=d:
                                            wet_floor += 1
                            
                            if wet_floor > max_wet_floor:
                                max_wet_floor = wet_floor
    print(max_wet_floor)

if __name__ == "__main__":
    main()