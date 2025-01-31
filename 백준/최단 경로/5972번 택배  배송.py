import sys
import heapq
input=sys.stdin.readline


n,m=map(int,input().split())
INF=int(1e9)

graph=[[] for i in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijsktra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist: # 힙정렬 되어서 최소로 나오는 건데 그것보다 작은것이므로 한번 계산이 된 것이므로 패스
            continue
        print("now",now)
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))


dijsktra(1)

print(distance[n])