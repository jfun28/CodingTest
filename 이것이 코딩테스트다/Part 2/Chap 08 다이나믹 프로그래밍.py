# # 피보나치 함수

# def fibo(x):
#     if x==1 or x==2:
#         return 1
#     return fibo(x-1)+fibo(x-2)

# print(fibo(99))


# 8-2.py 피보나치 수열 소스코드(재귀적)


# # 한 번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화

# d=[0]*100

# def fibo(x):
#     # 종료 조건(1 혹은 2일 때 1을 반환)
#     if x==1 or x==2:
#         return 1
#     # 이미 계산한 적 있는 문제라면 그대로 반환
#     if d[x]!=0:
#         return d[x]
#     # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반홙
#     d[x]=fibo(x-1)+fibo(x-2)
#     return d[x]

# print(fibo(99))

## 8-3.py 호출되는 함수 확인

# d=[0]*100

# def pibo(x):
#     print('f('+str(x)+')',end=' ')
#     if x==1 or x==2:
#         return 1
#     if d[x]!=0:
#         return d[x]
#     d[x]=pibo(x-1)+pibo(x-2)
#     return d[x]
# pibo(6)


# # 2 실전문제 1로 만들기

# # 1을 만든다는 점에서 피보나치와 상당히 유사한 점이 많다. 

# n=int(input())

# d=[0]*30001
# for i in range(2,n+1):
#     d[i]=d[i-1]+1
#     if i%2==0:
#         d[i]=min(d[i],d[i//3]+1)
#     if i%3==0:
#         d[i]=min(d[i],d[i//3]+1)
#     if i%5==0:
#         d[i]=min(d[i],d[i//5]+1)


# print(d[n])


# # 실전문제3 개미 전사

# n=int(input())

# array=list(map(int,input().split()))

# d=[0]*100

# d[0]=array[0]
# d[1]=max(array[0],array[1])

# for i in range(2,n):
#     d[i]=max(d[i-1],d[i-2]+array[i])


# print(d[n-1])

# # 실전 문제 4 바닥 공사

# n=int(input())

# d=[0]*1001

# # 다이나믹 프로그래밍 진행(보텀업)

# d[1]=1
# d[2]=3

# for i in range(3,n+1):
#     d[i]=(d[i-1]+2*d[i-2])%796796


# print(d[n])




























