# 백준 14501번
n=int(input())
t=[]
p=[]
di=[0]*(n+1)

for _ in range(n):
    x,y=map(int,input().split())
    t.append(x)
    p.append(y)

max_point=0
for i in range(n-1,-1,-1):

    day_time=t[i]+i

    if day_time<=n:
        di[i]=max(di[day_time]+p[i],max_point)
        max_point=di[i]

    else:
        di[i]=max_point



print(max_point)





























#
# n=int(input())
# t=[]
# p=[]
# dp=[0]*(n+1)
# max_value=0
#
# for i in range(n):
#     x,y=map(int,input().split())
#     t.append(x)
#     p.append(y)
#
#
# # 리스트 뒤에서부터 거꾸로 확인
# for i in range(n-1,-1,-1):
#     print("i",i)
#     time=t[i]+i
#
#     print("time",time)
#     # 상담이 기간 안에 끝나는 경우
#     if time<=n:
#     # 점화식에 맞게,현재까지의 최고 이익 계산
#         dp[i]=max(p[i]+dp[time],max_value) # dp 저장해 놓는게 i번 째 날부터 마지막 날(상담이 가능한 날)까지 포이트 저장 리스트
#         max_value=dp[i]
#     # 상담이 기간을 벗어나는 경우
#     else:
#         print("else",time)
#         dp[i]=max_value
#
#
# print(max_value)
