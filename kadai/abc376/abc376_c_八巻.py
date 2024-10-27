# 玩具と箱の大きさを大きい順に並び変えて全部入れてみる。玩具が入らなかった場合、その玩具が入る箱を購入する。2回目は -1 を出力し終わる

def main():
    N = int(input())
    toy_list = list(map(int, input().split()))
    toy_box_list = list(map(int, input().split()))
    toy_list.sort(reverse=True)
    toy_box_list.sort(reverse=True)
    # 購入済みフラグ
    purchased = False
    # 何もなかったら最小の玩具が入る玩具箱を買うことになる
    ans = min(toy_list)
    # for文を玩具の回数回したいため toy_box_list の末尾に -1 を追加(玩具が入らないかつlistの中で最小の値)
    toy_box_list.append(-1)
    
    for i in range(N):
        if toy_box_list[i] < toy_list[i]:
            if purchased:
                ans = -1
                break
            else:
                ans = toy_list[i]
                # 事前に追加しておいた -1 を消してその分購入した箱を toy_box_list に追加している
                del toy_box_list[-1]
                toy_box_list.insert(i, ans)

                purchased = True
                
    print(ans)

if __name__ == "__main__":
    main()