n=int(input())

calender=[0]*366
for _ in range(n):
    s,e= map(int,input().split())
    for i in range(s,e+1):
        calender[i]+=1

row=0 # 가로 길이
col=0 # 세로 길이
result=0
for day in calender:
    if day!=0: # 일정이 없는 날이 아닌 경우
        col=max(col,day)
        row+=1

    else : # 일정이 없을 때
        result+=row*col
        row=0
        col=0

result+=row*col # 마지막 남은 일정들 더해주기
print(result)

