# key が入力された値, value が index +1 の dict を作る。その後 key が -1 の value, その value が key の value ・・・って感じに値をとる
N = int(input())
A = list(map(int, input().split()))
index_and_input_dict = {}

for i in range(len(A)):
    index_and_input_dict[A[i]] = i+1
    
ans = []
next_key = -1
for _ in range(N):
    next_key = index_and_input_dict.get(next_key)
    ans.append(next_key)
print(*ans)


