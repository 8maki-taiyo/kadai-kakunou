def main():
    h, w, d = map(int, input().split())
    S = [list(input()) for _ in range(h)]
    ans = 0
    wet_floor_list = []
    wet = [[False]*w for _ in range(h)]
    
    # 加湿されている床をTureとし、Trueの上下左右を新たなTrueにする(listに追加することで実現)
    for i in range(h):
        for j in range(w):
            if S[i][j] == 'H':
                wet_floor_list.append((i, j, d))
                wet[i][j] = True
                ans += 1

    for (x, y, distance) in wet_floor_list:
        for [i, j] in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            xa = x + i
            ya = y + j
            if 0 <= xa < h and 0 <= ya < w and distance > 0 and wet[xa][ya] == False and S[xa][ya] == '.':
                wet[xa][ya] = True
                ans += 1
                wet_floor_list.append((xa, ya, distance - 1))

    print(ans)
    
if __name__ == "__main__":
    main()