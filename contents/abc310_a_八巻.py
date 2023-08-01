n,p,q,price_list = None,None,None,None

while True:
    n,p,q = map(int , input().split())
    if 1 <= n <=100 and 1 <= q < p <= 10**5:
        break
    print("再入力してください")

while True:
    price_list = [list(map(int, input().split()))]
    limit_over_count = 0
    for prices in price_list:
        for price in prices:
            if 1 > price or price > 10**5:
                limit_over_count += 1
    if limit_over_count == 0:
        break
    print("再入力してください")

pricelow = 0
for prices in price_list:
    for price in prices:
        if pricelow == 0 :
            pricelow = price

        if pricelow > price:
            pricelow = price

use_coupon_price = pricelow + q
print("")
if use_coupon_price > p :
    print(p)

else :
    print(use_coupon_price)
