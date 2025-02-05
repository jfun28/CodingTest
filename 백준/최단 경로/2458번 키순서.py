import sys
input=sys.stdin.readline

# 학생들의 수와 비교횟수
n,m=map(int,input().split())
parent=[set() for _ in range(n+1)]
child=[set() for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    parent[a].add(b)
    child[b].add(a)

# 자신의 자식들에게 자신의 부모 정보를 전달
# 자신의 부모들에게 자신의 자식 정보를 전달

for i in range(1,n+1):
    for j in child[i]:
        parent[j].update(parent[i])

    for j in parent[i]:
        child[j].update(child[i])

cnt = 0
for i in range(1,n+1):
    if len(parent[i])+len(child[i])==n-1:
        cnt += 1

# 최종적으로 i노드의 부모노드수와 자식노드수가 n-1이면 정확히 알 수 있다.
print(cnt)





# import sys
# # INF=sys.maxsize
# # 노드의 개수 및 간선의 개수를 입력받기
# input=sys.stdin.readline
# n,m=map(int,input().split())

# graph=[[0]*(n+1) for _ in range(n+1)]


# # 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
# for _ in range(m):
#     # A에서 B로 가는 비용은 C라고 설정
#     a,b=map(int,input().split())
#     graph[a][b]=1

# # 점화식에 따라 플로이드 워셜 알고리즘을 수행
# for k in range(1,n+1):
#     for a in range(1,n+1):
#         if graph[a][k]:  # a에서 k로 가는 경로가 있을 때만 확인
#             for b in range(1, n+1):
#                 if graph[k][b]:  # k에서 b로 가는 경로가 있을 때만 확인
#                     graph[a][b] = 1


# result = 0
# for i in range(1, n+1):
#     sum = 0
#     for j in range(1, n+1):
#         sum += graph[i][j] + graph[j][i] # 어떤 노드로 기준으로 나아가는것과 들어오는 경우 모두 다 체크크
#     if sum == n-1:
#         result += 1
# print(result)

# # 자기 순서를 알고있는 학생 수를 출력하는 것
