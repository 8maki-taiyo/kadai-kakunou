# 公式の解説を見ました
# https://atcoder.jp/contests/abc371/editorial/10921

from itertools import permutations

# グラフをlistで保持するメソッド
# 頂点1,2 が辺で結ばれていた場合 graph[0][1], graph[1][0]をTrueとして保持する
def graph_to_list(m, n):
    graph = [[False for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a - 1][b - 1] = True
        graph[b - 1][a - 1] = True
    return graph

def create_money_list(n):
    money_list = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n - 1):
        x = map(int, input().split())
        for j, a in enumerate(x):
            money_list[i][i + 1 + j] = a
    return money_list

def main():
    ans = 10**9
    for p in permutations(range(N)):
        cost = 0
        for i in range(N):
            for j in range(i + 1, N):
                if g[p[i]][p[j]] != h[i][j]:
                    cost += money_list[i][j]
        ans = min(ans, cost)

    print(ans)

if __name__ == "__main__":
    N = int(input())
    Mg = int(input())
    g = graph_to_list(Mg, N)
    Mh = int(input())
    h = graph_to_list(Mh, N)
    money_list = create_money_list(N)

    main()