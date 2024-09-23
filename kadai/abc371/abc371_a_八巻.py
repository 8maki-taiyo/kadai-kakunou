def main():
    S = input()
    
    # パターンが少ないので入力に応じた答えを辞書で作る
    ans_dict = {
        "< < <": "B",
        "< < >": "C",
        "< > >": "A",
        "> < <": "A",
        "> > <": "C",
        "> > >": "B"
    }
    
    print(ans_dict[S])
    
if __name__ == "__main__":
    main()