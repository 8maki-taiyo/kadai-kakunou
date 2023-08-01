"""Module providingFunction printing python version."""

n,m = map(int,input().split())
products = [list(map(int, input().split())) for _ in range(n)]
o = 0
ans = "NO"
while o < n:
    i = 0
    while i < n:
        if i != o:
            checker = 0
            if products[o][0] >= products[i][0]:
                checker += 1
            ability_num = 1
            counter = 1
            no_exist_counter = 0
            prolen = len(products[o])
            sublen = len(products[i])
            while ability_num <= m:
                j = 1
                k = 1
                procounter = 0
                subcounter = 0
                while j < prolen:
                    if products[o][j] == ability_num:
                        procounter += 1
                    j += 1
                while k < sublen:
                    if products[i][k] == ability_num:
                        subcounter += 1
                    k += 1
                if procounter == subcounter:
                    counter += procounter
                elif procounter == 0 and subcounter >= 1:
                    no_exist_counter += 1

                ability_num += 1
            if counter == prolen:
                checker += 1
            if products[o][0] > products[i][0] | no_exist_counter >= 1:
                checker += 1
            if checker == 3:
                ans = "YES"
        i += 1
    o += 1
print("")
print(ans)
