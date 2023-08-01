"""Module providingFunction printing python version."""
n,m,product_status_list = None,None,None

while True:
    n,m = map(int,input().split())
    if 2 <= n <= 100 and 1 <= m <= 100:
        break
    print("再入力してください")

while True:
    product_status_list = [list(map(int, input().split())) for _ in range(n)]
    for product_status in product_status_list:
        if 1 >product_status[0] or product_status[0] > product_status[1] > m:
            continue
        i = 2
        product_list = []
        while i < len(product_status):
            product_status_list.append(product_status[i])
        for product_fuc in product_list:
            if product_fuc < 

ans = "NO"
product1_index_counter = 0
for product1_status in product_status_list:
    product1_list = []
    i = 2
    while i < len(product1_status):
        product1_list.append(product1_status[i])
        i += 1
    product2_index_counter = 0
    for product2_status in product_status_list:
        product2_list = []
        j = 2
        while j < len(product2_status):
            product2_list.append(product2_status[j])
            j += 1

        if product1_index_counter != product2_index_counter:
            checker = 0
            if product1_status[0] >= product2_status[0]:
                checker += 1
            ability_num = 1
            counter = 0
            no_exist_counter = 0
            while ability_num <= m:
                pro1_counter = 0
                pro2_counter = 0
                for product1 in product1_list:
                    if product1 == ability_num:
                        pro1_counter += 1
                for product2 in product2_list:
                    if product2 == ability_num:
                        pro2_counter += 1
                if pro1_counter == pro2_counter:
                    counter += pro1_counter
                elif pro1_counter == 0 and pro2_counter >= 1:
                    no_exist_counter += 1

                ability_num += 1
            if counter == len(product1_list):
                checker += 1
            if product1_status[0] > product2_status[0] | no_exist_counter >= 1:
                checker += 1
            if checker == 3:
                ans = "YES"
        product2_index_counter += 1
    product1_index_counter += 1
print("")
print(ans)
