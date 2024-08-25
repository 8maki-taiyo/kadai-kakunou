import math

qty,final_line = map(int,input().split())
mozi_list = list(map(int,input().split()))

haba = max(math.ceil((sum(mozi_list)+qty-final_line)/final_line),max(mozi_list))

while(True):
    mozi_count = 0
    line_count = 1
    for mozi in mozi_list:
        if mozi_count+mozi <= haba:
            mozi_count+=mozi
        else:
            line_count += 1
            mozi_count = mozi
        mozi_count+=1
        
    if line_count == final_line:
        print(haba)
        break
    haba+=1
