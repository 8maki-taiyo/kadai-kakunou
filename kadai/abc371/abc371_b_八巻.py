def taro_check(house, gender, taro_exist_house):
    if gender=="F":
        return "No"
    if house in taro_exist_house:
        return "No"
    return "Yes"
             
def main():
    N, M = map(int, input().split())
    taro_exist_house = []
    ans_list = []

    for _ in range(M):
        house, gender = input().split()
        # 太郎と名づけるか判定
        check_result = taro_check(house, gender, taro_exist_house)
        
        # 太郎と名づけた家を記録
        if check_result=="Yes":
            taro_exist_house.append(house) 
        
        ans_list.append(check_result)
    
    for ans in ans_list:    
        print(ans)

if __name__ == "__main__":
    main()