room_qty = int(input())
room_info_list = [list(map(int,input().split())) for _ in range(room_qty-1)]

room_info_list.insert(0,[0,0,0,0])
room_info_list.insert(1,[0,0,0,0])

can_move_room = set()
flag = set()

def add_room_and_flag(room_number):
    flag.add(room_number)
    for i in range(2,len(room_info_list)):
        if room_info_list[i][0]== room_number:
            can_move_room.add(i)

ememy_qty = 0

for i in range(2,len(room_info_list)):
    if room_info_list[i][1]==1:
        ememy_qty+=1
add_room_and_flag(1)

power=1
kusuri=[]
breaked_enemy=0

while True:
    breaked_power = []
    can_move_copy = can_move_room.copy()
    for room_number in can_move_copy:
        if room_number in flag:
            continue
        if room_info_list[room_number][1]==1:
            if power>=room_info_list[room_number][2]:
                breaked_power.append(room_info_list[room_number][3])
                add_room_and_flag(room_number)
                breaked_enemy+=1
        if room_info_list[room_number][1]==2:
            kusuri.append(room_info_list[room_number][3])
            add_room_and_flag(room_number)
            
    if breaked_enemy == ememy_qty:
        print("Yes")
        break
    if len(kusuri)==0 and len(breaked_power)==0:
        print("No")
        break
    if len(breaked_power) == 0:
        power *= min(kusuri)
        kusuri.remove(min(kusuri))
    else:
        power += sum(breaked_power)

