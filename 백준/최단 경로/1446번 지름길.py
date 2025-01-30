import heapq
import sys
input=sys.stdin.readline

m,n=map(int,input().split())
INF=int(1e9)
# 수정된 코드
graph=[[] for i in range(n+2)]
graph=[[(i+1,1)] if i<n+1 else [] for i in range(n+2)]
distance=[INF]*(n+2)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))



def dijkstra(start=0):
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist: # 현재 노드가 이미 처리된 적 있는 노드라면 무시
            continue
        # 현재 노드와 연결되어 있는 다른 인접한 노드들을 확인

        for i in graph[now]:
            cost=dist+i[1]
            # 현재 노드를 거쳐서, 다른 노노드로 이동하는 거리가 더 짧은 경우
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start=0)

print(distance[n])
