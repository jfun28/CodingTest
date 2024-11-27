# 백준 1446번 지름길
import sys
import heapq
input=sys.stdin.readline

INF=int(1e9)
n,m=map(int,input().split())

start=0
graph=[[] for i in range(m+1)]
distance=[INF]*(m+1)
cal_dist=[]

for i in range(m):
    graph[i].append((i+1, 1))


for _ in range(n):
    a,b,c=map(int,input().split())
    if b>m:
        continue
    graph[a].append((b,c))

def find_load(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist, point=heapq.heappop(q)
        if distance[point]<dist:
            continue

        for i in graph[point]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost, i[0]))


find_load(start)
for i in range(1,m+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i]!=INF:
        cal_dist.append(distance[i])

print(distance[m])
                            















# # 개선된 버전의 다익스트라 알고리즘 복기

# import heapq
# import sys
# input=sys.stdin.readline
# INF=int(1e9)

# n,m=map(int,input().split())

# start=int(input())

# graph=[[] for i in range(n+1)]

# # 거리 저장 리스트
# distance=[INF]*(n+1)


# for _ in range(m):
#     a,b,c=map(int,input().split())
#     graph[a].append((b,c))
    

# def dijkstra(start):
#     q=[]
#     heapq.heappush(q,(0,start))
#     distance[start]=0
#     while q: # 큐가 비어있지 않다면
#         # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 
#         dist,now=heapq.heappop(q)

#         # 현재 노드 전에 한번 훑은건지 확인 
#         if distance[now]<dist:
#             continue

#         for i in graph[now]:
#             cost=dist+i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]]=cost
#                 heapq.heappush(q,(cost,i[0]))

# dijkstra(start)

# for i in range(1,n+1):
#     # 도달할 수 없는 경우, 무한이라고 출력
#     if distance[i]==INF:
#         print("INFINITY")
#     else:
#         print(distance[i])















# # 개선된 버전의 다익스트라 알고리즘 

# import heapq
# import sys
# input=sys.stdin.readline
# INF=int(1e9)

# #노드의 개수, 간선의 개수를 입력받기

# n,m=map(int,input().split())

# # 시작 노드 번호를 입력 받기

# start=int(input())

# # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기 
# graph=[[] for i in range(n+1)]

# #최단 거리 테이블을 모두 무한으로 초기화 

# distance=[INF]*(n+1)

# # 모든 간선 정보를 입력받기

# for _ in range(m):
#     a,b,c=map(int,input().split())
#     graph[a].append((b,c))

# def dijkstra(start):
#     q=[]

#     # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
#     heapq.heappush(q,(0,start))
#     distance[start]=0
#     while q: # 큐가 비어있지 않다면
#         # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 
#         dist, now= heapq.heappop(q)
#         # 현재 노드가 이미 처리된 적이 있는 노드라면 무시 
#         if distance[now]<dist:
#             continue

#         # 현재 노드와 연결괸 다른 인접한 노드들을 확인
#         for i in graph[now]:
#             cost=dist+i[1]
#             # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
#             if cost<distance[i[0]]:
#                 distance[i[0]]=cost
#                 heapq.heappush(q,(cost, i[0]))


# dijkstra(start)

# for i in range(1,n+1):
#     # 도달할 수 없는 뎡우 , 무한 INFINITY를 출력
#     if distance[i]==INF:
#         print("INFINITY")
#     else:
#         print(distance[i])











# # import sys 
# # input=sys.stdin.readline
# # INF=int(1e9)
# # n,m=map(int,input().split())

# # graph=[[] for i in range(n+1)]

# # start=int(input())

# # visited=[False]*(n+1)

# # # 최단 거리 테이블 
# # distance=[INF]*(n+1)

# # for _ in range(m):
# #     a,b,c=map(int,input().split())
# #     graph[a].append((b,c))

# # # 방문하지 않은 노드 중에서, 최단거리가 짧은 노드의 번호를 반환


# # def get_smallest_node():
# #     min_value=INF
# #     index=0 # 거리가 가장 짧은 인덱스
# #     for i in range(1,n+1):
# #         if distance[i]<min_value and visited[i]!=True:
# #             min_value=distance[i]
# #             index=i
# #     return index



# # def dijkstra(start): 
# #     distance[start]=0
# #     visited[start]=True
# #     for j in graph[start]:
# #         distance[j[0]]=j[1]

# #     # 시작노드를 제외하고 전체 노드에 대해서 n-1를 반복함
# #     for i in range(n-1):
# #         #현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
# #         now=get_smallest_node()
# #         visited[now]=True
# #         # 현재 노드와 연결된 다른 노드를 확인 
# #         for j in graph[now]:
# #             cost=distance[now]+j[1]
# #             if cost<distance[j[0]]:
# #                 distance[j[0]]=cost
# # dijkstra(start)

# # for i in range(1,n+1):
# #     if distance[i]==INF:
# #         print("INFINITY")

# #     else:
# #         print(distance[i])