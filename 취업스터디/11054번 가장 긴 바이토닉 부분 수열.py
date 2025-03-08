
import sys
input = sys.stdin.readline

N = int(input())
cache1 = [1]*(N)
cache2 = [1]*(N)
A = list(map(int, input().split()))

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            cache1[i] = max(cache1[i], cache1[j]+1)
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if A[j] < A[i]:
            cache2[i] = max(cache2[i], cache2[j]+1)

ans = 0
for i in range(N):
    ans = max(ans, cache1[i]+cache2[i]-1)
print(ans)










# import sys
# input=sys.stdin.readline
# n=int(input())

# case=list(map(int,input().split()))
# increase=[1]*n
# decrease=[1]*n

# for i in range(1,n):
#     for j in range(i):
#         if case[i]>case[j]:
#             increase[i]=max(increase[i],increase[j]+1)

# for i in range(n-1-1,-1,-1):
#     for j in range(n-1,i,-1):
#         if case[i]>case[j]:
#             decrease[i]=max(decrease[i],decrease[j]+1)

# result=[0]*n

# for i in range(n):
#     result[i]=max(result[i],increase[i]+decrease[i]-1) # 가운데 숫자가 중복될 것 이니깐깐

# print(max(result))















# import sys
# input=sys.stdin.readline
# n=int(input())

# case=list(map(int,input().split()))
# reverse_case=case[::-1]

# increase=[1]*n
# decrease=[1]*n

# for i in range(1,n):
#     for j in range(i):
#         if case[i]>case[j]:
#             increase[i]=max(increase[i],increase[j]+1)

#         if reverse_case[i]>reverse_case[j]:
#             decrease[i]=max(decrease[i],decrease[j]+1)

# result=[0]*n
# decrease=decrease[::-1]

# for i in range(n):
#     result[i]=max(result[i],increase[i]+decrease[i]-1)

# print(increase)
# print(decrease)

# print(max(result))