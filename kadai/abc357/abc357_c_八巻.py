def main():
    level = int(input())
    
    before_carpet = ["#"]
    
    if level == 0:
        return before_carpet
        
    for _ in range(level):
        before_side_len = len(before_carpet)
        side_len = before_side_len*3
        
        # 前のカーペットを元にカーペットを作成する
        now_carpet = []
        for i in range(side_len):
            li = []
            for j in range(side_len):
                li.append(before_carpet[i%before_side_len][j%before_side_len])
            now_carpet.append(li)
        
        # 真ん中のカーペットを白くする
        for i in range(before_side_len):
            for j in range(before_side_len):
                now_carpet[i+before_side_len][j+before_side_len] = "."
    
    
        before_carpet = now_carpet
    return now_carpet 
    
if __name__ == "__main__":
    carpet = main()
    
    for ans in carpet:
        print("".join(ans))