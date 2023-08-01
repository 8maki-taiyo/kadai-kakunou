n = int(input())
stick_list = [list(input().split()) for _ in range(n)]
type_stick_list =[]
counter = 0
for sticks in stick_list:
    for stick in sticks:
        restick = stick[::-1]
        if len(type_stick_list) == 0:
            type_stick_list.append(stick)
        if not stick in type_stick_list and not restick in type_stick_list:
            type_stick_list.append(stick)
print(len(type_stick_list))
