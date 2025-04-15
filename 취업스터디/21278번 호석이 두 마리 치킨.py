INF=int(1e9)

n,m=map(int,input().split())
graph=[]


#2차원 리스트를 만들고 모든값을 무한으로 초기화
graph=[[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가느 비용은 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

# 플로이드 워셜 알고리즘으로 모든 정점에서 모든 정점으로 가는 최소거리 구하기
for k in range(1,n+1): 
    for a in range(1,n+1): # 출발노드
        for b in range(1,n+1): # 도착노드
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

# 2개의 건물을 선택하여(예상 치킨집) 모든 집을 방문해서 걸리는 거리를 측정
min_sum=INF
result=list()

for i in range(1,n): # 건물 2개를 뽑는다
    for j in range(2,n+1):
        sum=0
        for k in range(1,n+1): # 모든 집을 방문하면서 거리를 측정
            sum+=min(graph[k][i],graph[k][j])*2 # k->i, k->j 중 짧은 거 선택해서 곱하기 2
        if sum <min_sum:
            min_sum=sum
            result=[i,j,sum]
print(*result)
