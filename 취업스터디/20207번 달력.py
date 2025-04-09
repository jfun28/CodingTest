import sys
input=sys.stdin.readline
n=int(input())
arr=[0]*366
ans=0

for i in range(n):
    start,end=map(int,input().split())
    while start<=end:
        arr[start]+=1
        start+=1

rows,cols=0,0

for i in range(366):
    if arr[i]==0:
        ans+=rows*cols
        rows,cols=0,0
        continue

    rows+=1
    cols=max()
print(ans+rows*cols)



# n=int(input())

# calender=[0]*366
# for _ in range(n):
#     s,e= map(int,input().split())
#     for i in range(s,e+1):
#         calender[i]+=1

# row=0 # 가로 길이
# col=0 # 세로 길이
# result=0
# print("calender",calender)

# for day in calender:
#     if day!=0: # 일정이 없는 날이 아닌 경우
#         row=max(col,day)
#         col+=1

#     else : # 일정이 없을 때
#         result+=row*col # 한번 스택 쌓인거 털고 초기화하기
#         row=0 
#         col=0

# result+=row*col # 마지막 남은 일정들 더해주기
# print(result)

