# str.count("a") は str の中で a が出現する回数を数える
# https://docs.python.org/ja/3.13/library/stdtypes.html#str.count 

def main():
    N = input()
    print("Yes" if N.count("1")==1 and N.count("2")==2 and N.count("3")==3 else "No")
    
if __name__ == "__main__":
    main()