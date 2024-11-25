# 001111000111001 -> 00 1111 000 111 00 1 のように同じ文字にグループ化してから入れ替える

def main():
    N, K = map(int, input().split())
    S = input()
    common_char_group = []
    group_list = [] # common_char_group の list
    
    # 同じ文字でグループ化する
    for s in S:
        if not common_char_group or s == common_char_group[-1]:
            common_char_group.append(s)
        else:
            group_list.append(common_char_group)
            common_char_group=[s]        
    if common_char_group:
        group_list.append(common_char_group)
    
    # 入れ替え
    if S[0]=="1":
        group_list[K*2-2], group_list[K*2-3] = group_list[K*2-3], group_list[K*2-2]
    else:
        group_list[K*2-1], group_list[K*2-2] = group_list[K*2-2], group_list[K*2-1]
    
    ans = ""
    for common_char in group_list:
        for ch in common_char:
            ans+=ch
    print(ans)
    
if __name__ == "__main__":
    main()