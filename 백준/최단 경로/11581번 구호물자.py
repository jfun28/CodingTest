#### 클로드 정답
import sys
input = sys.stdin.readline
INF = int(102)  # 무한대 값 설정

n = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    graph[a][a] = 0

# 그래프 입력 받기
for i in range(1, n):
    n_num = int(input())
    temp = list(map(int, input().split()))
    for j in temp:
        graph[i][j] = 1

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
print(graph)


# 사이클 체크
has_cycle = False
for i in range(1, n+1):
    for j in range(1, n+1):
        if 0<graph[1][j]!= INF:
            if i != j and graph[i][j] != INF and graph[j][i] != INF :
                has_cycle = True
                break
        if has_cycle:
            break

print("CYCLE" if has_cycle else "NO CYCLE")





# ### 답안지 본 정답
# import sys
# input = sys.stdin.readline
#   # 무한대 값 설정

# n = int(input())
# graph = [[0]*(n+1) for _ in range(n+1)]

# # 자기 자신으로 가는 비용은 0으로 초기화
# for a in range(1, n+1):
#     graph[a][a] = 0

# # 그래프 입력 받기
# for i in range(1, n):
#     n_num = int(input())
#     temp = list(map(int, input().split()))
#     for j in temp:
#         graph[i][j] = 1

# # 플로이드 워셜 알고리즘 수행
# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             if graph[a][k] and graph[k][b]:
#                 graph[a][b] = 1

# for i in range(1,n+1):
#     if graph[i][i] ==1 and graph[1][i]: # 싸이클이 도는 구조이므로 첫번째 구호 시점과 연결은 되어 있어야한다. 
#         print('CYCLE')
#         exit()
# print('NO CYCLE')






# import sys
# input=sys.stdin.readline
# INF=int(102)

# n=int(input())

# graph=[[0]*(n+1) for i in range(n+1)]


# # 자기 자신에서 자기 자신으로 가느 비용은 0으로 초기화
# for a in range(1,n+1):
#     for b in range(1,n+1):
#         if a==b:
#             graph[a][b]=0

# for i in range(1,n):
#     n_num=int(input())
#     temp=list(map(int,input().split()))
#     for j in temp:
#         graph[i][j]=1
#     temp=[]

# check=0
# # 점화식에 따라 플로이드 워셜 알고리즘을 수행
# for k in range(1,n+1):
#     for a in range(1,n+1):
#         for b in range(1,n+1):
#             if a==b and graph[a][k]+graph[k][b]>1:
#                 check+=1



# if check>=1:
#     print("CYCLE")
# else:
#     print("NO CYCLE")