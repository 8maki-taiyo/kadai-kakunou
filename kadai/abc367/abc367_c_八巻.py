# iteratool の product を使用すれば簡単にできそう
# https://docs.python.org/ja/3/library/itertools.html#itertools.product
#
# product('ABCD', 'xy')
# > ('A', 'x') ('A', 'y') ('B', 'x') ('B', 'y') ('C', 'x') ('C', 'y') ('D', 'x') ('D', 'y')
# 
# のような感じで簡単に直積が取れる

from itertools import product

def main():
    N, K = map(int, input().split())
    R = list(map(int, input().split()))
    
    # 入力例1 の場合だと [1, 2] [1] [1, 2, 3] を作り product に渡している
    for sequence in product(*[[j for j in range(1, i + 1)] for i in R]):
        if sum(sequence) % K == 0:
            print(*sequence)
    
if __name__ == "__main__":
    main()