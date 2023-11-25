busstop_qty,walking_time_to_busstop,walking_time_to_friendhouse = map(int,input().split())
busstop_list= [list(map(int,input().split())) for _ in range(busstop_qty-1)]
Q = int(input())
start_time_list = [int(input()) for _ in range(Q)]

for start_time in start_time_list:
    start_time += walking_time_to_busstop
    for busstop in busstop_list:
        while(True):
            if start_time%busstop[0]==0:
                break
            start_time+=1
        start_time+=busstop[1]
    print(start_time+walking_time_to_friendhouse)