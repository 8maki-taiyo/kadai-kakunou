# 3平方の定理 a**2 + b**2 = c**2 -> 直角三角形

def main():
    xa,ya = map(int,input().split())
    xb,yb = map(int,input().split())
    xc,yc = map(int,input().split())


    AB2 =(xa- xb) **2 +(ya-yb)**2
    BC2 =(xb- xc) **2 +(yb-yc)**2
    CA2 =(xc- xa) **2 +(yc-ya)**2
        

    if AB2 + BC2 == CA2 or BC2 + CA2 == AB2 or CA2 + AB2 == BC2:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()