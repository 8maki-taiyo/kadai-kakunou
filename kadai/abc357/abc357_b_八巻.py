def main():
    s = input()
    uppercase = 0
    lowercase = 0
    
    for mozi in s:
        # isupper() はstrの中身が全て大文字の場合Trueを返す
        if mozi.isupper():
            uppercase += 1
        else:
            lowercase += 1
    print(s.upper() if uppercase > lowercase else s.lower())
    
if __name__ == "__main__":
    main()